#!/usr/bin/env python3
"""
PDF Generator Utility

Converts markdown synthesis files to professional PDF format.
Used by all agent tools to generate final synthesis PDFs.

Usage:
    python scripts/pdf_generator.py input.md output.pdf --report-type natal
    python scripts/pdf_generator.py input.md --report-type life_arc
    python scripts/pdf_generator.py input.md --report-type transit
"""

import sys
import argparse
from pathlib import Path
import markdown
from weasyprint import HTML, CSS


def load_css_for_report_type(report_type: str, css_dir: Path) -> list:
    """
    Load CSS files based on report type.

    Args:
        report_type: One of 'natal', 'life_arc', 'transit', 'event'
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
        'transit': 'movement_based.css',
        'event': 'movement_based.css'
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
    title: str = "Astrology Report",
    report_type: str = "natal"
) -> str:
    """
    Convert markdown file to professional PDF using external CSS files.

    Args:
        markdown_path: Path to markdown file
        pdf_path: Output PDF path (defaults to same name with .pdf extension)
        title: Document title for PDF metadata
        report_type: Report type ('natal', 'life_arc', 'transit', 'event')

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

    # Convert markdown to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=[
            'tables',
            'fenced_code',
            'nl2br',
            'sane_lists',
            'smarty'
        ]
    )

    # DEPRECATED: Old embedded CSS (kept for reference, not used)
    # CSS is now loaded from external files in scripts/css/
    deprecated_css = """
    @page {
        size: letter;
        margin: 2.5cm;
        @top-center {
            content: string(chapter);
            font-size: 9pt;
            color: #666;
        }
        @bottom-center {
            content: counter(page);
            font-size: 9pt;
            color: #666;
        }
    }

    body {
        font-family: Helvetica, Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #000000;
        text-align: left;
        hyphens: auto;
    }

    h1 {
        color: #000000;
        font-size: 24pt;
        font-weight: bold;
        margin-top: 0;
        margin-bottom: 0.5em;
        page-break-after: avoid;
        border-bottom: 3px solid #000000;
        padding-bottom: 0.3em;
    }

    h2 {
        color: #000000;
        font-size: 18pt;
        font-weight: bold;
        margin-top: 1.5em;
        margin-bottom: 0.5em;
        page-break-after: avoid;
        border-bottom: 2px solid #000000;
        padding-bottom: 0.2em;
    }

    h3 {
        color: #000000;
        font-size: 14pt;
        font-weight: bold;
        margin-top: 1.2em;
        margin-bottom: 0.4em;
        page-break-after: avoid;
    }

    h4 {
        color: #000000;
        font-size: 12pt;
        font-weight: bold;
        margin-top: 1em;
        margin-bottom: 0.3em;
        page-break-after: avoid;
    }

    p {
        margin-top: 0;
        margin-bottom: 0.8em;
        orphans: 3;
        widows: 3;
    }

    ul, ol {
        margin-left: 1.5em;
        margin-bottom: 1em;
    }

    li {
        margin-bottom: 0.3em;
    }

    strong {
        color: #000000;
        font-weight: bold;
    }

    em {
        font-style: italic;
        color: #000000;
    }

    code {
        font-family: 'Courier New', monospace;
        font-size: 9pt;
        background-color: #f4f4f4;
        padding: 0.1em 0.3em;
        border-radius: 3px;
    }

    pre {
        background-color: #f8f8f8;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 1em;
        overflow-x: auto;
        margin-bottom: 1em;
        page-break-inside: avoid;
    }

    pre code {
        background-color: transparent;
        padding: 0;
    }

    table {
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 1em;
        page-break-inside: avoid;
    }

    th {
        background-color: #000000;
        color: white;
        font-weight: bold;
        padding: 0.5em;
        text-align: left;
        border: 1px solid #000000;
    }

    td {
        padding: 0.5em;
        border: 1px solid #ddd;
    }

    tr:nth-child(even) {
        background-color: #f9f9f9;
    }

    blockquote {
        margin-left: 2em;
        margin-right: 2em;
        padding-left: 1em;
        border-left: 4px solid #000000;
        color: #000000;
        font-style: italic;
        page-break-inside: avoid;
    }

    hr {
        border: none;
        border-top: 2px solid #000000;
        margin: 2em 0;
    }

    a {
        color: #000000;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    /* Special styling for astrology symbols */
    .symbol {
        font-size: 1.2em;
    }

    /* Page break controls */
    .page-break {
        page-break-before: always;
    }

    .no-break {
        page-break-inside: avoid;
    }
    """
    # NOTE: Old CSS above is DEPRECATED and NOT USED
    # CSS is now loaded from external files: scripts/css/base.css + type-specific CSS

    # Wrap HTML with proper document structure
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>{title}</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Generate PDF using external CSS files
    HTML(string=full_html).write_pdf(
        pdf_path,
        stylesheets=css_objects
    )

    print(f"✅ PDF generated: {pdf_path}")
    print(f"   Report type: {report_type}")
    print(f"   CSS files loaded: base.css + {report_type}-specific")
    print(f"   Size: {pdf_path.stat().st_size / 1024:.1f} KB")

    return str(pdf_path)


def main():
    parser = argparse.ArgumentParser(
        description='Convert markdown synthesis to professional PDF using external CSS'
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
        '--title',
        default='Astrology Report',
        help='Document title for PDF metadata'
    )
    parser.add_argument(
        '--report-type',
        choices=['natal', 'life_arc', 'transit', 'event'],
        default='natal',
        help='Report type determines CSS styling (default: natal)'
    )

    args = parser.parse_args()

    try:
        pdf_path = markdown_to_pdf(
            args.markdown_file,
            args.pdf_file,
            args.title,
            args.report_type
        )
        print(f"\n✨ Success! PDF ready at: {pdf_path}")

    except Exception as e:
        print(f"❌ Error generating PDF: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
