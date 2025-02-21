Work-in-progress!

E-commerce website with a pipeline for self-serving analytics, for an imaginary company (at the moment) selling oud products. I started this project to get practice in:
- Web development
- ETL pipelines
- Terraform for cloud IaC
- Test-driven development

Preview of the website:
...

Outline of the data pipeline:
...

**Reflections**

**Website Data Models**

By default, Django projects use sqlite models to store data, which are lightweight and limited. They are not capable of handling large amounts of data and prone to issues such as race conditions. For example, if multiple customers ordered the same item at exactly the same time, it could lead to unexpected results.

It was easy to reconfigure the models to the brilliant open-source PostgreSQL, which automatically optimises queries and has Multi-Version Concurrency Control to avoid any issues with high loads.