# Secure Coding Guide: Javascript

## Best Practices Checklist


### 🛡️ JavaScript/Node.js Security

**Dependencies:**
- [ ] Use `npm audit` regularly to check for vulnerabilities
- [ ] Keep dependencies updated with `npm update`
- [ ] Use `--audit` flag with npm install
- [ ] Consider using Snyk or GitHub Dependabot

**Code Security:**
- [ ] Validate all user input with libraries like Joi or Validator.js
- [ ] Use parameterized queries for database access
- [ ] Sanitize HTML output to prevent XSS
- [ ] Implement proper CORS policies
- [ ] Use HTTPS in production

**Authentication:**
- [ ] Use bcrypt for password hashing (not plain text or weak hashes)
- [ ] Implement proper session management
- [ ] Use environment variables for secrets (never hardcode)



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