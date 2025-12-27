import yaml # Library to read YAML files


def generate_mcp_tools(openapi_path):
    # Load OpenAPI YAML file
    with open(openapi_path, "r") as f:
        spec = yaml.safe_load(f)

    tools = [] # List to store generated tools
    
    # Iterate through API paths and methods
    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            tools.append({
                "name": f"{method}_{path.replace('/', '_')}",
                "description": details.get("summary", ""),
                "path": path,
                "method": method.upper()
            })

    return tools # Return generated tools


if __name__ == "__main__":
    # Generate tools from OpenAPI spec
    tools = generate_mcp_tools("../openapi/pizza_openapi.yaml")
    print(tools)
