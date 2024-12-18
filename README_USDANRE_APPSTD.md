# SECTION 1

## General Standards

All technical solutions and development efforts must meet the following General Standards:

**Governance and Business Case**: Technical solution efforts must be approved through the Information Resources Decision Board (IRDB) and have a valid business case and investment manager.

**Security**: Technical solutions must be provided through a secure connection and comply with security mandates and guidelines. Application development teams will need to coordinate with cyber security to identify and work with an assigned system Information Systems Security Officer (ISSO) and document security requirements as early in the process as possible.

**Product Owner (business responsibility)**: Technical solutions must have a designated product owner. A Product Owner understands the organization, the problem being solved, and can advocate for the product being built. Product Owners establish and carry the long-term vision of the product, implement a strategy, and guide its progress, as informed by user research. In addition, the Product Owner defines acceptance criteria, completes user acceptance testing, and manages the product backlog.

**Technical Owner (CIO)**: Technical solutions must have a designated CIO technical owner. The Technical Owner is essential to maintain the technical fit, solution architecture, and lifecycle management of the solutions.

Understand the business problem/Technical requirements: The role of CIO is to develop a technical solution to a business problem. Solutions to business problems must be discovered using Human Centered Design (HCD) principles. Both product and technical owners must document the problem in a way that will help the technical team determine appropriate technical requirements and its associated solution architecture.

**Authoritative**: Technical solutions must not overlap with or duplicate existing solutions and must be approved via solution architecture process for authoritative data source.

**Hosting**: Technical solutions must be hosted on an authorized and approved data center or platform, coordinated with the Forest Service CIO Data Center Hosting Branch Services and designated Solution Architects from the CIO.

**Environment**: There must be a separation between production, development, and test environments. Developers will not have any access beyond development environments without exception.

# SECTION 2

## Accessibility & Design Standards

All technical solutions and development efforts must meet the following accessibility and design standards:

**Accessibility**: Technical solutions must be accessible to individuals with disabilities in accordance with Section 508.

**Consistency**: Technical solutions must be consistent in look and feel in accordance with the Federal, USDA, and U.S. Forest Service design playbook.

**Mobile friendly**: Technical Solutions must be usable and function on mobile devices.

**Searchable**: Web pages must contain a search function, unless otherwise noted in business-use case.

**User-centered**: User interface designs must focus on user needs and include data-driven analysis.

**U.S. Web Design System**: Public-facing websites and digital services should use the U.S. Web Design System (USWDS 2.6) and meet specific requirements.

# SECTION 3

## Technical Standards

All technical solutions and development efforts must meet the following technical standards:

**Solution Architecture**: A top-level solution/technical architecture of the system must be established with input from the Solution Architect and must be approved by the Forest Service Architecture Review Board.

**Source Code Management**: All source code 100%-associated with an application along with its configurations must be stored in the official source code management system.

**Master Branch Management**: A master branch is live in the production environment and should have an archived copy under release following standard naming conventions. It must be deploy-ready all the time.

**Technology Stacks**: All technical solutions must follow the approved tech standard for application development. Exceptions to that standard must be approved by the NRE Forest Service CIO through the Mission Support Services (MSS) Assistant Director. 

**Continuous Integration and Compliance Validation**: All technical solutions must follow the Continuous Integration (CI) process for application code vulnerability scanning (with zero vulnerability), accessibility testing (90% minimum passing grade), and linting (flagging programming errors, bugs, stylistic errors, and suspicious constructs) on coding standards. All application codes must pass the quality gates with minimum passing grade before source code release or branch merger.

**Standard Configuration**: All solutions must be deployed on standard configuration provided by the CIO.

**Continuous Deployment and Release Management**: All applications must follow the continuous delivery and release process of the CIO. Automated testing is critical in continuous delivery once a system has completely passed all tests and ensured that all release management artifacts are in place for the entire software delivery lifecycle. This means that on top of having automated testing, you also have automated the release process, therefore making it possible to deploy your application at any point of time by clicking on a button. With Continuous Delivery, applications are able to comply with auditable artifacts for the release process with product owner-approval, linting, vulnerability scanning, 508 testing, security impact analysis, and relevant approvals to automatically deploy approved release to production.

**Minify**: JavaScript, as written, includes dead spaces that slow download and execution time. In all technical solutions, JavaScript files must be minimized to reduce transit time and help speed up page load.

**JAVA Development**: Currently, many applications in NRE utilize JAVA as the programming language and as a runtime engine. With the evolution of lightweight and open-source frameworks, JAVA-based development is considered legacy. Most importantly, JAVA (offered by Oracle) has become a license-based model which should be in consideration before any new development or modernization efforts select JAVA-based solutions. Open Source and lightweight framework must be considered and must be consulted with CIO Solution Architects.

**Employ Continuous Monitoring and Alerting**: Every application much have continuous monitoring as part of its production release. Continuous Monitoring automates the process of notifying individuals whether an item has passed or failed; it can also execute necessary steps when an alert occurs. Continuous Monitoring solutions include the following types of monitoring: Infrastructure Monitoring, Application Performance Monitoring, Log Management Monitoring, and Security Monitoring.

## Federal Mandates

All Forest Service applications and application solutions must follow Federal guidelines. These include, but are not limited to:

21st Century IDEA ACT – Digital Experience for Federal Public Websites
The 21st Century Integrated Digital Experience Act, otherwise known as the 21st Century IDEA, was signed into law in December 2018. The Act aims to improve the digital experience for government customers and reinforces existing requirements for federal public websites.
Section 508 - The Rehabilitation Act
Section 508 Standards are part of the Federal Acquisition Regulation (FAR) and address access for people with physical, sensory, or cognitive disabilities. They contain technical criteria specific to various types of technologies and performance-based requirements that focus on functional capabilities of covered products. Specific criteria covers software applications and operating systems, web-based information and applications, computers, telecommunications products, video and multi-media, and self-contained closed products.
M-13-13 – Open Data Policy – Managing Information as an Asset
This Memorandum establishes a framework to help institutionalize the principles of effective information management at each stage of the information’s life cycle to promote interoperability and openness.
M-15-14 - Management and Oversight of Federal Information Technology
The purpose of this memorandum is to provide implementation guidance for the Federal Information Technology Acquisition Reform Act (FITARA) and related information technology (IT) management practices.
M-16-21 – Federal Source Code Policy
This policy seeks to address these challenges by ensuring that new custom-developed Federal source code be made broadly available for reuse across the Federal Government.
M-16-19 – Data Center Optimization Initiative
This memorandum defines a framework for achieving the data center consolidation and optimization requirements of FITARA, the criteria for successful agency data center strategies, and the metrics used to evaluate the success of those strategies.
M-11-11 - Guidelines for PIV-enablement, applicable to USDA guidelines
This memorandum mandates LincPass (HSPD-12) or PIV-enabled credentials to access federal information systems. The mandate requires that agencies use the PIV-enabled identification standard to the maximum extent practicable; therefore, exceptions to using PIV credentials must be justified by extenuating circumstances.
Authentication: All application authentication must use USDA authorized eAuthentication for web-based applications with PIV-enablement and enforcement. All other authentication, including usage of loging.gov or enterprise active directory, will require approval from CIO Cyber Security and Solution Architecture group within CIO AD (Application Development) branch.
Authorization: All applications must have access control setup, which allows support for multiple roles such as administrator, regular user with functional roles.
Account Re-certification: Accounts must be re-certified annually for users that continue to require access. Accounts must be deactivated if not re-certified or if not used for one year.
M-15-13 - The HTTPS-only Standard
This Memorandum requires that all publicly accessible Federal websites and web services only provide service through a secure connection. The strongest privacy and integrity protection currently available for public web connections is Hypertext Transfer Protocol Secure (HTTPS).
NIST FIPS-199 - Standards for Security Categorization of Federal Information and Information Systems
Each application must be categorized with a rating of low, moderate, or high impact in each category of confidentiality, integrity, and availability. All PII data is encrypted and stored as per NIST FIPS-200 and NIST 800-53 guidelines with strong authentication.

## References:
+ [21st Century IDEA ACT](https://digital.gov/resources/21st-century-integrated-digital-experience-act/?utm_source=listserv-allcop&utm_medium=email&utm_campaign=web-standards-2020-01-23)
+ [Section 508](https://digital.gov/resources/21st-century-integrated-digital-experience-act/?utm_source=listserv-allcop&utm_medium=email&utm_campaign=web-standards-2020-01-23)
+ [M-13-13 Open Data Policy](https://digital.gov/resources/21st-century-integrated-digital-experience-act/?utm_source=listserv-allcop&utm_medium=email&utm_campaign=web-standards-2020-01-23)
+ [M-15-14 Management and Oversight of Federal Information Technology](https://policy.cio.gov/fitara/)
+ [Federal Information Technology Acquisition Reform Act (FITARA)](https://www.congress.gov/113/plaws/publ291/PLAW-113publ291.pdf#page=148)
+ [M-16-21 Federal Source Code Policy] (https://policy.cio.gov/source-code/)
+ [Data Center Optimization Initiative](https://policy.cio.gov/dcoi/)
+ [Guidelines for PIV-enablement](http://www.cac.mil/Portals/53/Documents/m-11-11.pdf?ver=2017-04-17-081020-897
+ [HTTPS-only Standard](https://www.whitehouse.gov/sites/whitehouse.gov/files/omb/memoranda/2015/m-15-13.pdf)
+ [NIST FIPS-199](http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.199.pdf)
