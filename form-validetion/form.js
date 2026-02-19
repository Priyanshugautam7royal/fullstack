const form = document.getElementById("contact-form");

const nameInput = document.getElementById("contact-name");
const phoneInput = document.getElementById("contact-phone");
const emailInput = document.getElementById("contact-email");
const messageInput = document.getElementById("contact-message");

const nameError = document.getElementById("name-error");
const phoneError = document.getElementById("phone-error");
const emailError = document.getElementById("email-error");
const messageError = document.getElementById("message-error");
const submitError = document.getElementById("submit-error");

function validateName() {
    const name = nameInput.value.trim();

    if (name === "") {
        nameError.textContent = "Name is required";
        return false;
    }

    if (!/^[A-Za-z]+\s[A-Za-z]+$/.test(name)) {
        nameError.textContent = "Enter full name (First Last)";
        return false;
    }

    nameError.textContent = "";
    return true;
}

function validatePhone() {
    const phone = phoneInput.value.trim();

    if (phone === "") {
        phoneError.textContent = "Phone is required";
        return false;
    }

    if (!/^[0-9]{10}$/.test(phone)) {
        phoneError.textContent = "Phone must be 10 digits";
        return false;
    }

    phoneError.textContent = "";
    return true;
}

function validateEmail() {
    const email = emailInput.value.trim();

    if (email === "") {
        emailError.textContent = "Email is required";
        return false;
    }

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        emailError.textContent = "Invalid email format";
        return false;
    }

    emailError.textContent = "";
    return true;
}

function validateMessage() {
    const message = messageInput.value.trim();

    if (message.length < 10) {
        messageError.textContent = "Minimum 10 characters required";
        return false;
    }

    messageError.textContent = "";
    return true;
}

form.addEventListener("submit", function (e) {
    e.preventDefault();

    const isNameValid = validateName();
    const isPhoneValid = validatePhone();
    const isEmailValid = validateEmail();
    const isMessageValid = validateMessage();

    if (isNameValid && isPhoneValid && isEmailValid && isMessageValid) {
        submitError.style.color = "green";
        submitError.textContent = "Form submitted successfully!";
        form.reset();
    } else {
        submitError.style.color = "red";
        submitError.textContent = "Please fix the errors above.";
    }
});

nameInput.addEventListener("keyup", validateName);
phoneInput.addEventListener("keyup", validatePhone);
emailInput.addEventListener("keyup", validateEmail);
messageInput.addEventListener("keyup", validateMessage);
