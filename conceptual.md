### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

  - is a powerful database management system

- What is the difference between SQL and PostgreSQL?

  - SQL

- In `psql`, how do you connect to a database?

  - SQL is a standardized language for querying and managing databases, while PostgreSQL is a specific database management system that utilizes SQL as its query language while offering its own unique features

- What is the difference between `HAVING` and `WHERE`?
  - WHERE filters individual rows before the grouping (if any) takes place, in the other hand, HAVING filters groups of rows based on aggregate values after the grouping has been applied.
- What is the difference between an `INNER` and `OUTER` join?

  - An inner join returns all the rows from the tables that are matching, while outer returns all the rows from one table, and the matching ones for the other one

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

  - the left outer is going to use the left table as the main one, and return the matching rows from the right one, and the right outer is going to return all the rows from the right one, and the matching from the left one

- What is an ORM? What do they do?

  - stands for Object-Relational Mapping. It's a programming technique used in software development that helps developers work with databases using an object-oriented approach, a popular one with python is SQLAlchemy

- What are some differences between making HTTP requests using AJAX
  and from the server side using a library like `requests`?

  - Initiation: AJAX requests are initiated from the client-side (usually a web browser) using JavaScript. meanwhile request are initiated in the back-end, these requests happen in the backend
  - Usage: AJAX is commonly used in web development to fetch data from a server or to send data to a server in the background, in the other hand, request is used to make http requests to other servers to do the same as AJAx and consuming apis
  - AJAX request cannot make requests to a different domain unless CORS is configured on the serverside, requests can do this without CORS

- What is CSRF? What is the purpose of the CSRF token?

  - CSRF stands for Cross-Site Request Forgery. It is a type of attack where a malicious website, email, or other source tricks a user's browser into making an unintended request to a different site where the user is authenticated. This attack occurs because the victim's browser includes existing authentication credentials (e.g., session cookies) when making requests to the target website.

- What is the purpose of `form.hidden_tag()`?
  - The form.hidden_tag() function is specifically used to include hidden fields in a form that might contain sensitive information or tokens required for security measures like CSRF protection
