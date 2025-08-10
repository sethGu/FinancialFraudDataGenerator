
# 🐳 Deployment Guide (Docker)

This page provides a quick guide for deploying **F²-Gen** using Docker and Docker Compose. This method is recommended for users who want an isolated, reproducible environment without manually setting up dependencies.

> 💡 For manual (non-Docker) setup instructions, see the [Deployment Instructions (Non-Docker)](deploy.html).  
> 📘 For usage guidance and system walkthrough, refer to the [Usage Guide](usage.html) and [Demo Video](demo.html).  
> ⚙️ For technical details, see the [Engine Overview](engine.html) and [Technical Report](technical.html).

---

## 🚀 Quick Start

 Install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/) to quickly get started with the project.

---

### 1. Clone the Git Repository

First, clone the code repository to the local directory：

```bash
git clone https://github.com/sethGu/FinancialFraudDataGenerator.git
cd generate-visualization-main
```

---

### 2. Build Docker Images

Run the following command to build the required Docker images:

```bash
docker-compose build
```

---

### 3. Create Docker Volumes

Create Docker volumes for the database and application data:

```bash
docker volume create --name=vol_smart_pgdata
docker volume create --name=vol_smart_data
```

> 📌 You can rename volumes if needed, but make sure to reflect the change in `docker-compose.yml`.

---

### 4. Run Database Migrations

Ensure that the database is initialized and run the migration command:

```bash
docker-compose run --rm backend python manage.py dbcheck
docker-compose run --rm backend python manage.py migrate
```

---

### 5. Start the Application
Start all the containers:

```bash
docker-compose up -d
```

---

### 6. Access the Platform

Once all containers are running, open your browser and visit:

👉 **[http://localhost:9528](http://localhost:9528)**

Login using the default credentials:

```text
🔐 Username: editor
🔐 Password: FdpDg@2024
```

---

## Note

When you use the Docker mode. Comment out `'HOST': '127.0.0.1'` in the `generate-visualization-main/backend/web/setting.py` file and uncomment `'HOST': 'db'`; in the `smart_finance_main/src/utils/config.py` file, comment out `host='localhost'` and uncomment `host='db'`.

---

## 📦 Download

You can also download the platform source code from the latest release:

<div style="margin-top: 1em; margin-bottom: 1em;">
  <a href="https://github.com/sethGu/FinancialFraudDataGenerator/releases/download/v1.0/F2Gen-v1.0.zip" style="text-decoration: none;">
    <button style="background-color: #007acc; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-weight: bold;">
      ⬇️ Download .zip
    </button>
  </a>
</div>

---

## 🧩 Additional Resources

- 📘 [Usage Guide](usage.html)  
- 📊 [Engine Overview](engine.html)  
- 📄 [Technical Report](technical.html)  
- 🔧 [Deployment Instructions (Non-Docker)](deploy.html)  
- 🎬 [Demo Walkthrough](demo.html)
