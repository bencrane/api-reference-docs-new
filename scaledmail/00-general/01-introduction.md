# Scaledmail API Documentaion

**Welcome to Scaledmail! Let’s get you authenticated and ready to build. 🛠️**

---

### **🔑 Finding Your API Key**

Your **API key** is used to authenticate all incoming requests. Each key is unique to your Scaledmail account and has access to all organizations under that account.

To get your API key, go to:

👉 **[https://app.scaledmail.com/settings](https://app.scaledmail.com/settings)**

---

### **🔐 Authentication**

All API requests must include a **Bearer token** in the `Authorization` header.

Example:

```bash

curl --location 'https://server.scaledmail.com/api/v1/organizations' \

--header 'Authorization: Bearer YOUR_API_KEY'

```

Replace `YOUR_API_KEY` with your actual token.

This ensures that requests are securely authenticated and authorized to access your Scaledmail account.

---

### **📌 Required Parameter: `organization_id`**

All endpoints require an `organization_id`.

Each organization is a separate environment within your account for managing domains, inboxes, and campaigns.

Be sure to include `organization_id` in every request.

---

### **📉 Rate Limits**

* **Limit:** 5 requests per second

* **Note:** Exceeding the limit may result in temporary blocks.

---

### **❓ Need Help or More Endpoints?**

We’re here to support you!

Reach out to us at **[support@scaledmail.com](mailto:support@scaledmail.com)** for any assistance or feature requests.

