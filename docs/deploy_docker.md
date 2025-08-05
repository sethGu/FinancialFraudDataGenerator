
# 🐳 Deployment Guide (Docker)

This page provides a quick guide for deploying **F²-Gen** using Docker and Docker Compose. This method is recommended for users who want an isolated, reproducible environment without manually setting up dependencies.

> 💡 For manual (non-Docker) setup instructions, see the [Deployment Instructions (Non-Docker)](deploy.html).  
> 📘 For usage guidance and system walkthrough, refer to the [Usage Guide](usage.html) and [Demo Video](demo.html).  
> ⚙️ For technical details, see the [Engine Overview](engine.html) and [Technical Report](technical.html).

---

## 🚀 Quick Start

Install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/) to get started.

---

### 1. Clone the Git Repository

```bash
git clone https://github.com/sethGu/FinancialFraudDataGenerator.git
cd FinancialFraudDataGenerator
```

---

### 2. Build Docker Images

```bash
docker-compose build
```

---

### 3. Create Docker Volumes

```bash
docker volume create --name=vol_f2gen_pgdata
docker volume create --name=vol_f2gen_data
```

> 📌 You can rename volumes if needed, but make sure to reflect the change in `docker-compose.yml`.

---

### 4. Run Database Migrations

```bash
docker-compose run --rm backend python manage.py migrate
docker-compose run --rm backend python manage.py createsuperuser
```

---

### 5. Start the Application

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
