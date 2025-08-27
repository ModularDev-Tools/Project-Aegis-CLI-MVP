# Secure Coding Guide: Python

## Best Practices Checklist


### 🐍 Python Security

**Dependencies:**
- [ ] Use `pip audit` or safety check
- [ ] Keep dependencies updated regularly
- [ ] Use virtual environments for isolation
- [ ] Consider using pip-tools for dependency management

**Code Security:**
- [ ] Validate all user input with libraries like Cerberus or Pydantic
- [ ] Use parameterized queries for database access (never string formatting)
- [ ] Sanitize HTML output to prevent XSS
- [ ] Be cautious with eval() and exec()

**Authentication:**
- [ ] Use bcrypt or Argon2 for password hashing
- [ ] Implement proper session management
- [ ] Use environment variables for secrets
- [ ] Consider using libraries like Authlib for OAuth



## General Security Principles

- [ ] Principle of Least Privilege
- [ ] Defense in Depth
- [ ] Never trust user input
- [ ] Keep software dependencies updated
- [ ] Regular security audits
- [ ] Proper error handling (don't leak sensitive info)

## Resources

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- GitHub Security: https://docs.github.com/en/code-security
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework

---

*This guide was generated using [Project Aegis CLI](https://github.com/JamesTheGiblet/Project-Aegis-CLI). Customize it for your project's specific needs.*