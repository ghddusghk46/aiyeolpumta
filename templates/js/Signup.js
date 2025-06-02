const id = document.querySelector(".id-field");
const password = document.querySelector(".password-field");
const rePassword = document.querySelector(".re-password-field");
const username = document.querySelector(".username-field");

const signupButton = document.querySelector(".signup-button");

function signup() {
  if (
    id.value === "" ||
    password.value === "" ||
    rePassword.value === "" ||
    username.value === ""
  ) {
    alert("모든 필드를 입력해주세요.");
    return;
  }

  if (password.value !== rePassword.value) {
    alert("비밀번호가 일치하지 않습니다.");
  }

  if (
    password.value.length < 8 ||
    !/[A-Z]/.test(password.value) ||
    !/[!@#$%^&*(),.?":{}|<>]/.test(password.value)
  ) {
    alert(
      "비밀번호는 8자 이상이며, 대문자와 특수문자를 각각 하나 이상 포함해야 합니다."
    );
    return;
  }

  const userData = {
    id: id.value,
    password: password.value,
    username: username.value,
    createdAt: new Date().toISOString(),
  };

  fetch("http://localhost:3000/api/users", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(userData),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

signupButton.addEventListener("click", signup);
