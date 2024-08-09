🔗 Reference: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

В этом документе приводятся рекомендации для разработки грамотной логики авторизации пользователей:

- [Enforce Least Privileges](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html#enforce-least-privileges)
- [Deny by Default](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html#deny-by-default)
- [Validate the Permissions on Every Request](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html#validate-the-permissions-on-every-request)
- [Thoroughly Review the Authorization Logic of Chosen Tools and Technologies, Implementing Custom Logic if Necessary](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html#thoroughly-review-the-authorization-logic-of-chosen-tools-and-technologies-implementing-custom-logic-if-necessary)
- [Prefer Attribute and Relationship Based Access Control over RBAC](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html#prefer-attribute-and-relationship-based-access-control-over-rbac)
- [Ensure Lookup IDs are Not Accessible Even When Guessed or Cannot Be Tampered With](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html#ensure-lookup-ids-are-not-accessible-even-when-guessed-or-cannot-be-tampered-with)
- [Enforce Authorization Checks on Static Resources](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html#enforce-authorization-checks-on-static-resources)
- [Verify that Authorization Checks are Performed in the Right Location](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html#verify-that-authorization-checks-are-performed-in-the-right-location)
- [Exit Safely when Authorization Checks Fail](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html#exit-safely-when-authorization-checks-fail)
- [Implement Appropriate Logging](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html#implement-appropriate-logging)
- [Create Unit and Integration Test Cases for Authorization Logic](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html#create-unit-and-integration-test-cases-for-authorization-logic)

----
Authorization may be defined as "the process of verifying that a requested action or service is approved for a specific entity" ([NIST](https://csrc.nist.gov/glossary/term/authorization)).

Authorization is distinct from authentication which is the process of verifying an entity's identity. When designing and developing a software solution, it is important to keep these distinctions in mind. A user who has been authenticated (perhaps by providing a username and password) is often not authorized to access every resource and perform every action that is technically possible through a system. For example, a web app may have both regular users and admins, with the admins being able to perform actions the average user is not privileged to do so, even though they have been authenticated.

Additionally, authentication is not always required for accessing resources; an unauthenticated user may be authorized to access certain public resources, such as an image or login page, or even an entire web app.