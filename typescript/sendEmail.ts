import nodemailer from "nodemailer";

interface EmailOptions {
    mail: string;
    subject: string;
    message: string;
}

const sendEmail = async (options: EmailOptions): Promise<void> => {
    const transporter = nodemailer.createTransport({
        host: process.env.SMTP_HOST as string,
        port: parseInt(process.env.SMTP_PORT as string),
        auth: {
            user: process.env.SMTP_USER as string,
            pass: process.env.SMTP_PASS as string,
        },
    });

    const message = {
        from: process.env.FROM_EMAIL as string,
        to: options.mail,
        subject: options.subject,
        text: options.message,
    };

    await transporter.sendMail(message);
};

export default sendEmail;
