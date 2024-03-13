## Nodemailer Email Sender

This npm package offers a straightforward utility function for sending emails through Nodemailer.

**Installation**

This project supports the following lanuages, See the language specific guide:

- javascript
- typescript
- python(not published)

**Usage**

1.  **Import the Function:**

Begin by importing the `sendEmail` function from the package:

- JavaScript

```
npm install send-email-util

```

- python

```
pip install send-email-util

```

- typescript

```
npm install send-email-util

```

2.  **Send Emails:**

Utilize the `sendEmail` function, passing an object containing email details:

JavaScript

```
import sendEmail from "send-email-util/javascript/sendEmail.js";

// Example usage
const emailObject = {
  mail: "recipient@example.com",
  subject: "Subject of the email",
  message: "Content of the email",
};

await sendEmail(emailObject);

```

python

```
from send-email-util.python.send_email import send_email

email_object = {
'mail': 'recipient@example.com',
'subject': 'Subject of the email',
'message': 'Content of the email',
}

send_email(email_object)

```

typescript

```
import sendEmail from "send-email-util/typescript/sendEmail.js";


const emailObject = {
    mail: "recipient@example.com",
    subject: "Subject of the email",
    message: "Content of the email",
};

await sendEmail(emailObject);

```

**Note**

- Replace `"recipient@example.com"` with the recipient's email address.

- Replace `"Subject of the email"` with the desired subject line.

- Replace `"Content of the email"` with the email body content.

**Configuration**

This package relies on environment variables for SMTP configuration. Ensure you have these set:

- `SMTP_HOST`: SMTP server hostname

- `SMTP_PORT`: SMTP server port

- `SMTP_USER`: SMTP username

- `SMTP_PASS`: SMTP password

You can define these environment variables in a `.env` file or directly within your deployment environment.

**🚀Future plans/ideas**

- add support for lanuages like python , typescript and golang

- Credential Management: Shift away from hardcoded credentials towards secure storage methods like environment variables.

- Input Validation: Implement rigorous validation to prevent injection attacks and ensure only valid input is accepted.

- Error Handling: Implement robust error handling to prevent leakage of sensitive information.

- Authentication & Authorization: Strengthen mechanisms for authentication and authorization, including encryption and secure session management.

**Contribution**

- if you have any issue or have a idea which can improve this , feel free to Raise a PR or open a new issue

**Contact me**

- Abhishek kumar (Twitter): [@abhirajabhi312](https://twitter.com/abhirajabhi312)
