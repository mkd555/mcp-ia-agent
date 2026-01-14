from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MY_MCP_SERVER")

@mcp.tool()
def get_infos_about_employee(name: str)-> str:
    """Get infos about a employee given his name:
    - First Name
    - Last Name
    - Age
    - City
    - Salary
    - Email
    """
    employee_info = {
        "First Name": name,
        "Last Name":"Mamadou",
        "Age": 25,
        "City": "Dakar",
        "Salary": 5000,
        "Email":"mkd@gmail.com"
    }
    # Format the dict into a readable string
    info_str = "\n".join([f"{key}: {value}" for key, value in employee_info.items()])
    return info_str