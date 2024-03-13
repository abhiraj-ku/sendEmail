## Nodemailer Email Sender

This npm package offers a straightforward utility function for sending emails through Nodemailer.

**Installation**

To incorporate this package into your project, use npm:

```
npm install nodemailer-email-sender

```

**Usage**

1.  **Import the Function:**

    Begin by importing the `sendEmail` function from the package:

    JavaScript

    ```
    import sendEmail from "nodemailer-email-sender";

    ```

2.  **Send Emails:**

    Utilize the `sendEmail` function, passing an object containing email details:

    JavaScript

    ```
    const emailObject = {
        mail: "recipient@example.com",
        subject: "Subject of the email",
        message: "Content of the email",
    };

    await sendEmail(emailObject);

    ```

    - Replace `"recipient@example.com"` with the recipient's email address.
    - Replace `"Subject of the email"` with the desired subject line.
    - Replace `"Content of the email"` with the email body content.

**Example: Sending an Email Verification Token**

Here's an illustrative example of sending an email verification token:

JavaScript

```
const emailObject = {
    mail: user.email.address,
    subject: "Email verification token",
    message: "Your verification token is: <token>",
};

await sendEmail(emailObject);

```

- Replace `<token>` with the actual verification token you intend to send.

**Configuration**

This package relies on environment variables for SMTP configuration. Ensure you have these set:

- `SMTP_HOST`: SMTP server hostname
- `SMTP_PORT`: SMTP server port
- `SMTP_USER`: SMTP username
- `SMTP_PASS`: SMTP password

You can define these environment variables in a `.env` file or directly within your deployment environment.

**Contribution**

- if you have any issue or have a idea which can improve this , feel free to Raise a PR or open a new issue
