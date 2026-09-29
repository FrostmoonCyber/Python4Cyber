# Import Console, Table, Panel, etc. from rich
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.table import Table

# Define static test data dictionary
MOCK_AUDIT_DATA = {
    "target": "https://example-target.com",
    "status": "SUCCESS",
    "headers": {
        "Strict-Transport-Security": "PRESENT",
        "Content-Security-Policy": "MISSING",
        "X-Frame-Options": "PRESENT",
        "X-Content-Type-Options": "MISSING"
    }
}

def render_audit_report(data: dict) -> None:
    # 1. Initialize rich Console
    console = Console()
    # 2. Build or print a header/panel with target and overall status
    table = Table(title ="Security Headers Audit", header_style="bold_magenta" ) 
    # 3. Instantiate Table with appropriate titles and column formatting
    #    Example columns: "Security Header", "Status"
    table.add_column("Header",justify="left", style="bold magenta") 
    table.add_column("Status", justify="left", style="bold cyan")
    
    
    # 4. Iterate over data["headers"]:
    #    - If status is "PRESENT", format with green color tag
    #    - If status is "MISSING", format with red color tag
    #    - Add row to table
    for header_name, status in data["headers"].items():
        if status == "PRESENT":
            formatted_status = "[green]PRESENT[/green]"
        else: 
            formatted_status = "[red]MISSING[/red]"
            
        table.add_row(header_name, formatted_status)



    
    # 5. Print table to console
    console.print(table)
if __name__ == "__main__":
    # Test your function with MOCK_AUDIT_DATA
    pass