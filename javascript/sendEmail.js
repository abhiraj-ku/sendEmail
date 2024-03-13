import nodemailer from "nodemailer";

/**
 * Sends an email using Nodemailer.
 * @param {Object} options - Email options.
 * @param {string} options.mail - Recipient's email address.
 * @param {string} options.subject - Subject of the email.
 * @param {string} options.message - Body of the email.
 */
const sendEmail = async (options) => {
  // Create a transporter with SMTP configuration
  const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST, // SMTP server hostname
    port: process.env.SMTP_PORT, // SMTP server port

    // SMTP authentication credentials
    auth: {
      user: process.env.SMTP_USER, // SMTP username
      pass: process.env.SMTP_PASS, // SMTP password
    },
  });

  // Create email message object
  const message = {
    from: process.env.FROM_EMAIL, // Sender's email address
    to: options.mail, // Recipient's email address
    subject: options.subject, // Subject of the email
    text: options.message, // Body of the email
  };

  // Send the email using the transporter
  await transporter.sendMail(message);
};

export default sendEmail;

// Author: Abhishek Kumar
// GitHub: https://github.com/abhiraj-ku/sendEmail
