🍕 Mission: Make Pizza AI-Ready

This project demonstrates how a traditional pizza ordering system can be adapted to work in an AI-driven ecosystem where AI agents act as the primary interface instead of humans using websites or mobile applications.

The core idea of this assignment is to make existing APIs usable by AI agents. As AI systems such as ChatGPT and Copilot become more common, applications must expose structured, predictable, and agent-friendly interfaces. This project focuses on achieving that goal using a lightweight, mock-based backend and agent-oriented design.

The system consists of an AI-ready backend built using FastAPI. This backend exposes pizza-related APIs such as menu listing, order placement, and order tracking. These APIs return structured responses containing fields like order ID, price, and estimated preparation time, making them suitable for consumption by AI agents.

An ordering agent is included to demonstrate how natural language input can be converted into structured API calls. For example, a user command like “I want a small cheese n corn pizza” is interpreted by the agent, which then calls the backend API with the appropriate pizza name and size.

The project also includes a scheduling agent to demonstrate readiness for agent-to-agent communication. While the scheduling workflow is kept simple, the architecture supports extending this agent to integrate with external MCP-enabled services such as calendars or delivery systems.

Pricing logic is handled entirely on the backend to ensure consistency across all consumers, including the UI and AI agents. Each pizza has a base price defined for the medium size. The final price is calculated using size-based multipliers, where small size is half the base price, medium size is the base price, and large size is one and a half times the base price.

A Streamlit-based user interface is included only for demonstration purposes. The UI consumes the same backend APIs that AI agents use, proving that the system is truly AI-ready. The UI does not contain any business logic and serves only as a visualization layer.

This solution satisfies the assignment requirements by converting traditional APIs into AI-consumable interfaces, supporting natural language ordering, producing structured responses suitable for agent workflows, and demonstrating readiness for multi-agent coordination. The backend is intentionally lightweight and mock-based, as instructed, with the focus placed on architecture and agent compatibility rather than complex backend implementation.

This project reflects my own understanding, design decisions, and implementation approach. The documentation and explanations are intentionally written in a clear and simple manner to accurately represent my thought process throughout the assignment.
