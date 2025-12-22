{

    "servers": {

        "upstash/context7": {

            "type": "http",

            "url": "https://mcp.context7.com/mcp",

            "headers": {

                "CONTEXT7_API_KEY": "ctx7sk-14379d91-db3c-4525-8c5f-2810367ddda4"

            },

            "gallery": "https://api.mcp.github.com/2025-09-15/v0/servers/dcec7705-b81b-4e0f-8615-8032604be7ad",

            "version": "1.0.0"

        },

        "microsoft/playwright-mcp": {

            "type": "stdio",

            "command": "npx",

            "args": [

                "@playwright/mcp@latest"

            ],

            "gallery": "https://api.mcp.github.com/2025-09-15/v0/servers/41b79849-7e6c-4fc7-82c0-5a611ea21523",

            "version": "0.0.1-seed"

        },

        "microsoft/markitdown": {

            "type": "stdio",

            "command": "uvx",

            "args": [

                "markitdown-mcp==0.0.1a4"

            ],

            "gallery": "https://api.mcp.github.com/2025-09-15/v0/servers/976a2f68-e16c-4e2b-9709-7133487f8c14",

            "version": "1.0.0"

        },

        "graphiti": {

            "type": "http",

            "url": "http://8.138.81.161:8000/mcp/"

        }

    }

}