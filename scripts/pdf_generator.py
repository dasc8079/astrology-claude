#!/usr/bin/env python3
"""
Enhanced PDF Generator with Front Matter System

Converts markdown synthesis files to professional PDF format with:
- Title page (cover)
- Table of Contents
- Chart Overview / Instructions page
- Full introduction section
- Main report content

Usage:
    python scripts/pdf_generator.py input.md --seed-data profiles/Name/seed_data/seed_data.json --report-type natal
    python scripts/pdf_generator.py input.md --seed-data seed_data.json --report-type life_arc
    python scripts/pdf_generator.py input.md --seed-data seed_data.json --report-type transit_short
"""

import sys
import argparse
import json
import yaml
import re
from pathlib import Path
from datetime import datetime
import markdown
from weasyprint import HTML, CSS


def load_seed_data(seed_data_path: Path) -> dict:
    """
    Load seed data from JSON or YAML file.

    Tries YAML first (common format), then JSON.

    Args:
        seed_data_path: Path to seed_data.json or .yaml file

    Returns:
        Dictionary containing seed data
    """
    if not seed_data_path.exists():
        raise FileNotFoundError(f"Seed data file not found: {seed_data_path}")

    with open(seed_data_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Try YAML first (most common format)
    try:
        return yaml.safe_load(content)
    except yaml.YAMLError:
        pass

    # Fall back to JSON
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Could not parse seed data as YAML or JSON: {e}")


def extract_big_three(seed_data: dict) -> tuple:
    """
    Extract Sun, Moon, Rising signs from seed data.

    Args:
        seed_data: Seed data dictionary

    Returns:
        Tuple of (sun_sign, moon_sign, rising_sign)
    """
    planets = {p['name']: p for p in seed_data.get('planets', [])}

    sun_sign = planets.get('Sun', {}).get('sign', 'Unknown')
    moon_sign = planets.get('Moon', {}).get('sign', 'Unknown')
    rising_sign = seed_data.get('chart_framework', {}).get('ascendant', {}).get('sign', 'Unknown')

    return sun_sign, moon_sign, rising_sign


def extract_chart_overview_data(seed_data: dict, report_type: str) -> dict:
    """
    Extract data for Chart Overview section based on report type.

    Args:
        seed_data: Seed data dictionary
        report_type: Report type (natal, life_arc, transit_short, transit_long)

    Returns:
        Dictionary with relevant overview data
    """
    data = {}

    if report_type == 'natal':
        # Natal Chart Overview data
        sect_type = seed_data.get('chart_framework', {}).get('sect', {}).get('type', 'unknown')
        data['sect'] = f"{sect_type.capitalize()} chart"

        # Chart ruler
        houses = seed_data.get('houses', [])
        first_house = houses[0] if houses else {}
        ruler_info = first_house.get('ruler', {})
        ruler_planet = ruler_info.get('planet', 'Unknown')
        ruler_position = ruler_info.get('position', {})
        ruler_sign = ruler_position.get('sign', 'Unknown')
        ruler_house = ruler_position.get('house', '?')
        ruler_dignities = ruler_position.get('dignities', 'peregrine')

        data['chart_ruler'] = f"{ruler_planet} in {ruler_sign} in {ruler_house}th house ({ruler_dignities})"

        # Angular planets
        angular_planets = []
        for planet in seed_data.get('planets', []):
            if planet.get('dignities', {}).get('accidental', {}).get('angular'):
                angular_planets.append(f"{planet['name']} ({planet['house']}th)")
        data['angular_planets'] = ', '.join(angular_planets) if angular_planets else 'None'

        # Stelliums
        stelliums = seed_data.get('stelliums', [])
        stellium_strs = []
        for stell in stelliums:
            planets = ', '.join(stell['planets'])
            stellium_strs.append(f"{stell['count']} planets in {stell['location']} ({planets})")
        data['stelliums'] = '; '.join(stellium_strs) if stellium_strs else 'None'

        # Key dignities (domicile/exaltation)
        dignities = []
        for planet in seed_data.get('planets', []):
            ess = planet.get('dignities', {}).get('essential', {})
            if ess.get('domicile'):
                dignities.append(f"{planet['name']} domicile in {planet['sign']}")
            elif ess.get('exaltation'):
                dignities.append(f"{planet['name']} exalted in {planet['sign']}")
        data['key_dignities'] = '; '.join(dignities[:3]) if dignities else 'None'

        # Major aspects (< 3° orb)
        aspects = seed_data.get('aspects', [])
        major_aspects = [
            f"{asp['planet_1']}-{asp['planet_2']} {asp['aspect_type']} ({asp['orb']:.2f}°)"
            for asp in aspects if asp.get('orb', 99) < 3.0 and asp.get('traditional', False)
        ]
        data['major_aspects'] = '; '.join(major_aspects[:3]) if major_aspects else 'None'

    elif report_type == 'life_arc':
        # Life Arc Overview data
        from datetime import datetime

        # Get birth date and calculate current age
        birth_data = seed_data.get('birth_data', {})
        birth_date_str = birth_data.get('date', '')

        current_age = None
        if birth_date_str:
            try:
                birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
                today = datetime.now()
                current_age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            except:
                pass

        data['current_age'] = current_age if current_age else 'Unknown'

        # Get ZR Fortune L1 current chapter
        # Note: This requires life arc data to be embedded in seed_data or passed separately
        # For now, extract if available in seed_data metadata
        metadata = seed_data.get('metadata', {})
        life_arc_data = metadata.get('life_arc_data', {})

        if life_arc_data:
            zr_fortune = life_arc_data.get('zr_fortune', {})
            l1_periods = zr_fortune.get('l1_periods', [])

            # Find current L1 period
            current_l1 = None
            if current_age and l1_periods:
                for period in l1_periods:
                    if period['start_age'] <= current_age < period['end_age']:
                        current_l1 = period
                        break

            if current_l1:
                data['current_chapter'] = f"{current_l1['sign']} (ages {current_l1['start_age']}-{current_l1['end_age']})"
            else:
                data['current_chapter'] = 'Data not available'

            # List major chapters (past, current, future)
            major_chapters = []
            for period in l1_periods[:5]:  # Show first 5 L1 periods
                age_range = f"ages {period['start_age']}-{period['end_age']}"
                major_chapters.append(f"{period['sign']} ({age_range})")
            data['major_chapters'] = '; '.join(major_chapters) if major_chapters else 'Data not available'
        else:
            data['current_chapter'] = 'Calculate with life_arc_generator.py'
            data['major_chapters'] = 'Calculate with life_arc_generator.py'

        # Profection year (can calculate from current age)
        if current_age:
            profected_house = ((current_age % 12) + 1)
            data['profection_year'] = f"House {profected_house} year (age {current_age})"
        else:
            data['profection_year'] = 'Unknown'

        # Progression themes (if available in metadata)
        progression_themes = metadata.get('progression_themes', [])
        if progression_themes:
            data['progression_themes'] = '; '.join(progression_themes[:2])
        else:
            data['progression_themes'] = 'See life arc chapters for timing'

    elif report_type in ['transit_short', 'transit_long']:
        # Transit Context data (TODO: implement when transit data structure finalized)
        data['note'] = 'Transit context data not yet implemented'

    return data


def parse_markdown_headings(md_content: str) -> list:
    """
    Parse markdown content to extract headings for Table of Contents.

    Args:
        md_content: Raw markdown content

    Returns:
        List of dicts with {level, title, description} for each heading
    """
    headings = []
    lines = md_content.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Match headings
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            title = line.lstrip('#').strip()

            # Extract first paragraph after heading as description (for life arc TOC)
            description = ''
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1  # Skip blank lines
            if j < len(lines):
                # Get first paragraph (up to 100 words or blank line)
                desc_lines = []
                while j < len(lines) and lines[j].strip() and not lines[j].startswith('#'):
                    desc_lines.append(lines[j].strip())
                    j += 1
                    if len(' '.join(desc_lines).split()) > 100:
                        break
                description = ' '.join(desc_lines)[:200]  # Limit to ~200 chars

            headings.append({
                'level': level,
                'title': title,
                'description': description
            })

        i += 1

    return headings


def build_title_page(seed_data: dict, report_type: str, sun_sign: str, moon_sign: str, rising_sign: str) -> str:
    """
    Build HTML for title page (Page 1).

    Args:
        seed_data: Seed data dictionary
        report_type: Report type
        sun_sign, moon_sign, rising_sign: Big Three signs

    Returns:
        HTML string for title page
    """
    # Zodiac sign symbols
    sign_symbols = {
        'Aries': '♈', 'Taurus': '♉', 'Gemini': '♊',
        'Cancer': '♋', 'Leo': '♌', 'Virgo': '♍',
        'Libra': '♎', 'Scorpio': '♏', 'Sagittarius': '♐',
        'Capricorn': '♑', 'Aquarius': '♒', 'Pisces': '♓'
    }

    # Convert sign names to symbols
    sun_symbol = sign_symbols.get(sun_sign, sun_sign)
    moon_symbol = sign_symbols.get(moon_sign, moon_sign)
    rising_symbol = sign_symbols.get(rising_sign, rising_sign)

    # Report title mapping
    title_map = {
        'natal': 'Natal Horoscope',
        'life_arc': 'Life Arc Report',
        'transit_short': 'Transit Report',
        'transit_long': 'Long-Term Transit Analysis'
    }

    title = title_map.get(report_type, 'Astrology Report')

    # Extract birth data
    birth_data = seed_data.get('birth_data', {})
    date_str = birth_data.get('date', 'Unknown date')
    time_str = birth_data.get('time', 'Unknown time')
    location = birth_data.get('location', 'Unknown location')
    lat = birth_data.get('latitude', 0)
    lon = birth_data.get('longitude', 0)

    # Format coordinates
    lat_dir = 'N' if lat >= 0 else 'S'
    lon_dir = 'E' if lon >= 0 else 'W'
    coords = f"{abs(lat):.4f}°{lat_dir}, {abs(lon):.4f}°{lon_dir}"

    # Profile name
    profile_name = seed_data.get('metadata', {}).get('profile_name', 'Unknown')
    display_name = profile_name.replace('_', ' ')

    # Generation date
    gen_date = datetime.now().strftime('%B %d, %Y')

    html = f'''
    <div class="title-page">
        <h1 class="report-title">{title}</h1>
        <div class="profile-name">{display_name}</div>
        <div class="birth-data">
            Born: {date_str} at {time_str}<br>
            {location}<br>
            {coords}
        </div>
        <div class="big-three">
            ☉ {sun_symbol} • ☽ {moon_symbol} • ↗ {rising_symbol}
        </div>
        <div class="generation-date">Report Generated: {gen_date}</div>
    </div>
    <div class="page-break"></div>
    '''

    return html


def build_table_of_contents(headings: list, report_type: str) -> str:
    """
    Build HTML for Table of Contents (Page 2).

    Args:
        headings: List of heading dicts from parse_markdown_headings()
        report_type: Report type (affects whether to include descriptions)

    Returns:
        HTML string for TOC
    """
    html = '<div class="toc-page">\n<h2>Table of Contents</h2>\n<div class="toc-content">\n'

    # Note about page numbers
    html += '<p class="toc-note"><em>Page numbers will be implemented in future PDF generation enhancements</em></p>\n'

    for heading in headings:
        level = heading['level']
        title = heading['title']
        description = heading['description']

        # Skip h1 "Introduction" and "Reflection" from detailed TOC (show as simple entries)
        if level == 1:
            html += f'<div class="toc-item-main"><strong>{title}</strong></div>\n'
        elif level == 2:
            # For life_arc, include descriptions; for others, simple list
            if report_type == 'life_arc' and description:
                html += f'<div class="toc-item-chapter">\n'
                html += f'  <div class="toc-chapter-title">{title}</div>\n'
                html += f'  <div class="toc-chapter-desc">{description}</div>\n'
                html += f'</div>\n'
            else:
                html += f'<div class="toc-item-sub">• {title}</div>\n'
        elif level == 3:
            # Show more H3 headings for better navigation
            html += f'<div class="toc-item-subsub">  - {title}</div>\n'

    html += '</div>\n</div>\n<div class="page-break"></div>\n'

    return html


def build_chart_overview_page(seed_data: dict, report_type: str) -> str:
    """
    Build HTML for Chart Overview + Instructions (Page 3).

    Args:
        seed_data: Seed data dictionary
        report_type: Report type

    Returns:
        HTML string for overview page
    """
    # "How to Use This Report" blurbs
    usage_blurbs = {
        'natal': '''<p>This natal horoscope synthesizes traditional Hellenistic astrological methods with psychological depth to reveal your inherent patterns, strengths, and growth edges. The interpretation is based on your birth chart calculated for the exact moment and location of your birth. Read this as a map of potentials, not fixed predictions—astrology describes archetypal energies that you have the agency to express in multiple ways. The chart overview below provides technical reference points for those familiar with astrological terminology.</p>''',

        'life_arc': '''<p>This life arc report traces the major chapters and transitions of your life from birth to age 100 using traditional timing techniques (Zodiacal Releasing, profections, progressions, and planetary returns). Each life phase carries distinct themes and challenges. The timeline below highlights when significant shifts occur—use this as a roadmap to understand past patterns and anticipate future transitions. Current age is marked to show where you stand in your life story. Remember that astrology reveals timing and themes, but your choices shape how these energies manifest.</p>''',

        'transit_short': '''<p>This transit report analyzes the current and upcoming planetary movements affecting your natal chart over the next several months. Transits reveal windows of opportunity, challenge, and growth—not fixed events. The timing context below shows where you are in longer life cycles (Zodiacal Releasing chapters, profection year) that provide the "frame" for understanding these shorter-term transits. Use this report as a weather forecast: you can't control the weather, but you can prepare and respond skillfully.</p>''',

        'transit_long': '''<p>This long-term transit analysis maps major planetary movements over the next several years, organized by thematic chapters rather than calendar months. Slow-moving outer planets (Saturn, Jupiter, Uranus, Neptune, Pluto) create multi-year narratives that unfold in phases. The timing context below shows your current position in major life cycles—these longer chapters provide essential context for understanding why transits manifest as they do. This is not predictive fortune-telling, but rather a framework for conscious participation in your unfolding story.</p>'''
    }

    # "About the Chart Overview" blurbs
    about_blurbs = {
        'natal': '''<p><strong>About the Chart Overview Below:</strong> The chart overview provides key astrological data points from your birth chart—sect (day/night), chart ruler, angular planets, dignities, and major aspect patterns. This technical reference is for those familiar with astrological terminology and serves as a quick-reference snapshot of your chart's most significant features.</p>''',

        'life_arc': '''<p><strong>About the Timeline Below:</strong> The timeline shows major life events and chapter transitions extracted from your life arc analysis. Ages and experiences are written in accessible language to give you a one-page preview of your life's major turning points. Current age is marked with an arrow.</p>''',

        'transit_short': '''<p><strong>About the Timing Context Below:</strong> The timing context shows where you currently are in your longer life cycles (Zodiacal Releasing chapters, profection year, active L2 periods) and which major transits are active during this report period. This "frame" is essential for understanding why transits manifest differently at different life stages.</p>''',

        'transit_long': '''<p><strong>About the Timing Context Below:</strong> The timing context shows where you currently are in your longer life cycles (Zodiacal Releasing chapters, profection year, active L2 periods) and which major transits are active during this report period. This "frame" is essential for understanding why transits manifest differently at different life stages.</p>'''
    }

    usage_text = usage_blurbs.get(report_type, usage_blurbs['natal'])
    about_text = about_blurbs.get(report_type, about_blurbs['natal'])

    # Build Chart Overview content based on report type
    overview_data = extract_chart_overview_data(seed_data, report_type)

    overview_html = '<div class="chart-overview-content">\n'

    if report_type == 'natal':
        # Check for output_mode in seed data metadata
        output_mode = seed_data.get('metadata', {}).get('output_mode', 'Standard')

        overview_html += '<h3>Chart Overview</h3>\n<ul class="chart-data-list">\n'
        overview_html += f'<li><strong>Output Mode:</strong> {output_mode}</li>\n'
        overview_html += f'<li><strong>Sect:</strong> {overview_data.get("sect", "Unknown")}</li>\n'
        overview_html += f'<li><strong>Chart Ruler:</strong> {overview_data.get("chart_ruler", "Unknown")}</li>\n'
        overview_html += f'<li><strong>Angular Planets:</strong> {overview_data.get("angular_planets", "None")}</li>\n'
        overview_html += f'<li><strong>Stelliums:</strong> {overview_data.get("stelliums", "None")}</li>\n'
        overview_html += f'<li><strong>Key Dignities:</strong> {overview_data.get("key_dignities", "None")}</li>\n'
        overview_html += f'<li><strong>Major Aspects:</strong> {overview_data.get("major_aspects", "None")}</li>\n'
        overview_html += '</ul>\n'
    elif report_type == 'life_arc':
        overview_html += '<h3>Life Arc Overview</h3>\n<ul class="chart-data-list">\n'
        overview_html += f'<li><strong>Current Age:</strong> {overview_data.get("current_age", "Unknown")}</li>\n'
        overview_html += f'<li><strong>Current Chapter:</strong> {overview_data.get("current_chapter", "Data not available")}</li>\n'
        overview_html += f'<li><strong>Profection Year:</strong> {overview_data.get("profection_year", "Unknown")}</li>\n'
        overview_html += f'<li><strong>Major Life Chapters:</strong> {overview_data.get("major_chapters", "Data not available")}</li>\n'
        overview_html += f'<li><strong>Progression Themes:</strong> {overview_data.get("progression_themes", "See chapters for timing")}</li>\n'
        overview_html += '</ul>\n'
    elif report_type in ['transit_short', 'transit_long']:
        overview_html += '<p><em>Transit timing context will be displayed here (structure pending)</em></p>\n'

    overview_html += '</div>\n'

    # Combine into full page
    html = f'''
    <div class="overview-page">
        <h2>How to Use This Report</h2>
        {usage_text}

        {about_text}

        {overview_html}
    </div>
    <div class="page-break"></div>
    '''

    return html


def build_full_html_with_front_matter(md_content: str, seed_data: dict, report_type: str, title: str) -> str:
    """
    Build complete HTML with 4-page front matter + main content.

    Args:
        md_content: Raw markdown content from interpreter
        seed_data: Seed data dictionary
        report_type: Report type
        title: Document title for metadata

    Returns:
        Complete HTML ready for WeasyPrint
    """
    # Extract Big Three
    sun_sign, moon_sign, rising_sign = extract_big_three(seed_data)

    # Parse headings for TOC
    headings = parse_markdown_headings(md_content)

    # Build front matter pages
    title_page = build_title_page(seed_data, report_type, sun_sign, moon_sign, rising_sign)
    toc_page = build_table_of_contents(headings, report_type)
    overview_page = build_chart_overview_page(seed_data, report_type)

    # Convert markdown to HTML
    main_content_html = markdown.markdown(
        md_content,
        extensions=[
            'tables',
            'fenced_code',
            'nl2br',
            'sane_lists',
            'smarty',
            'toc'
        ]
    )

    # Assemble full HTML
    full_html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>{title}</title>
    </head>
    <body>
        {title_page}
        {toc_page}
        {overview_page}
        {main_content_html}
    </body>
    </html>
    '''

    return full_html


def load_css_for_report_type(report_type: str, css_dir: Path) -> list:
    """
    Load CSS files based on report type.

    Args:
        report_type: One of 'natal', 'life_arc', 'transit_short', 'transit_long'
        css_dir: Path to CSS directory (scripts/css/)

    Returns:
        List of CSS objects to apply
    """
    css_objects = []

    # Always load base.css first
    base_css_path = css_dir / 'base.css'
    if base_css_path.exists():
        css_objects.append(CSS(filename=str(base_css_path)))
    else:
        print(f"⚠️  Warning: base.css not found at {base_css_path}")

    # Load report-type-specific CSS
    type_css_map = {
        'natal': 'chart_based.css',
        'life_arc': 'timeline_based.css',
        'transit_short': 'movement_based.css',
        'transit_long': 'movement_based.css'
    }

    if report_type in type_css_map:
        type_css_path = css_dir / type_css_map[report_type]
        if type_css_path.exists():
            css_objects.append(CSS(filename=str(type_css_path)))
        else:
            print(f"⚠️  Warning: {type_css_map[report_type]} not found at {type_css_path}")
    else:
        print(f"⚠️  Warning: Unknown report type '{report_type}', using base.css only")

    return css_objects


def markdown_to_pdf(
    markdown_path: str,
    pdf_path: str = None,
    seed_data_path: str = None,
    title: str = "Astrology Report",
    report_type: str = "natal"
) -> str:
    """
    Convert markdown file to professional PDF with front matter.

    Args:
        markdown_path: Path to markdown file
        pdf_path: Output PDF path (defaults to same name with .pdf extension)
        seed_data_path: Path to seed_data.json or .yaml file (REQUIRED for front matter)
        title: Document title for PDF metadata
        report_type: Report type ('natal', 'life_arc', 'transit_short', 'transit_long')

    Returns:
        Path to generated PDF
    """
    markdown_path = Path(markdown_path)

    if not markdown_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {markdown_path}")

    # Default PDF path: same name, .pdf extension
    if pdf_path is None:
        pdf_path = markdown_path.with_suffix('.pdf')
    else:
        pdf_path = Path(pdf_path)

    # Load seed data (required for front matter)
    if seed_data_path is None:
        raise ValueError("--seed-data is required for front matter generation")

    seed_data = load_seed_data(Path(seed_data_path))

    # Determine CSS directory (scripts/css/ relative to this file)
    script_dir = Path(__file__).parent
    css_dir = script_dir / 'css'

    # Load CSS files based on report type
    css_objects = load_css_for_report_type(report_type, css_dir)

    if not css_objects:
        raise FileNotFoundError(f"No CSS files found in {css_dir}")

    # Read markdown content
    with open(markdown_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Build complete HTML with front matter
    full_html = build_full_html_with_front_matter(md_content, seed_data, report_type, title)

    # Generate PDF using external CSS files
    HTML(string=full_html).write_pdf(
        pdf_path,
        stylesheets=css_objects
    )

    print(f"✅ PDF generated: {pdf_path}")
    print(f"   Report type: {report_type}")
    print(f"   CSS files loaded: base.css + {report_type}-specific")
    print(f"   Front matter: Title page, TOC, Chart Overview, Introduction")
    print(f"   Size: {pdf_path.stat().st_size / 1024:.1f} KB")

    return str(pdf_path)


def main():
    parser = argparse.ArgumentParser(
        description='Convert markdown synthesis to professional PDF with front matter'
    )
    parser.add_argument(
        'markdown_file',
        help='Input markdown file path'
    )
    parser.add_argument(
        'pdf_file',
        nargs='?',
        help='Output PDF file path (optional, defaults to same name with .pdf)'
    )
    parser.add_argument(
        '--seed-data',
        required=True,
        help='Path to seed_data.json or .yaml file (REQUIRED for front matter)'
    )
    parser.add_argument(
        '--title',
        default='Astrology Report',
        help='Document title for PDF metadata'
    )
    parser.add_argument(
        '--report-type',
        choices=['natal', 'life_arc', 'transit_short', 'transit_long'],
        default='natal',
        help='Report type determines CSS styling and front matter (default: natal)'
    )

    args = parser.parse_args()

    try:
        pdf_path = markdown_to_pdf(
            args.markdown_file,
            args.pdf_file,
            args.seed_data,
            args.title,
            args.report_type
        )
        print(f"\n✨ Success! PDF ready at: {pdf_path}")

    except Exception as e:
        print(f"❌ Error generating PDF: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
