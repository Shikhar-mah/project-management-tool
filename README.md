# 📘 AI-Powered Project Management System

## 🧾 Project Overview

This project is a **full-stack Project Management System** built using FastAPI (backend) and Streamlit (frontend), designed to manage projects, users, tasks, and collaboration through comments. It provides an intuitive interface and a robust backend to handle real-world task management workflows.

A key highlight of this system is the integration of **AI-powered automation**, which enhances task creation by:

* Automatically generating task descriptions
* Suggesting task priorities based on context

The application enables users to:

* Create and manage projects
* Assign tasks to users
* Track task progress through different stages
* Collaborate using a comment system
* Visualize tasks in a structured board (Kanban-style)

---

## 🎯 Key Objectives

* Provide a centralized system for managing:

  * Projects
  * Tasks
  * Users
  * Comments
* Enable seamless task assignment and tracking
* Improve productivity through AI-assisted task enrichment
* Deliver an interactive UI for better usability

---

## ⚙️ Core Features

### 📁 Project Management

* Create, update, and delete projects
* Organize tasks under specific projects

---

### 👤 User Management

* Create and manage users
* Assign tasks to users

---

### 📋 Task Management

* Create tasks within projects
* Assign tasks to users
* Track task status:

  * TODO
  * IN PROGRESS
  * COMPLETED

---

### 💬 Comment System

* Add comments to tasks
* View task-specific discussions
* Enables team collaboration

---

### 🤖 AI Integration

* Auto-generates task descriptions
* Suggests priority levels:

  * LOW
  * MEDIUM
  * HIGH

---

### 📊 Interactive Dashboard (Streamlit)

* View projects, users, and tasks
* Kanban-style task board
* Filter tasks by project and user
* Perform CRUD operations visually

---

## 🧠 System Design Philosophy

The system is built using a **clean layered architecture** to ensure:

* **Separation of Concerns**

  * API layer handles requests
  * Service layer handles logic
  * Repository layer handles database operations

* **Scalability**

  * Easily extendable for new features like authentication, notifications, etc.

* **Maintainability**

  * Modular code structure with clear responsibilities 

* **Extensibility**

  * AI services are abstracted and can be upgraded independently

---

## 🚀 Use Cases

* Team-based project tracking
* Task assignment and monitoring
* Internal productivity tools
* AI-assisted task management systems

---

## 📂 Project Structure Overview

The project is divided into backend and frontend components: 

### Backend (`app/`)

* API routes
* Services (business logic)
* Repositories (DB layer)
* Models & schemas

### Frontend (`Frontend/`)

* Streamlit-based UI dashboard

---

## 📌 Summary

This project serves as a **modern, AI-enhanced project management solution**, combining structured backend design with an interactive frontend. It is suitable as a foundation for building scalable productivity tools and can be extended into a full enterprise-grade system.

---
