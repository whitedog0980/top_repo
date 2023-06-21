import './beforeMig/css.css'

function Register () {
  return (
    <>
      <nav className="navigate">
        <span id="loginSpan">
          <a href="login.html" className="btn btn-info loginLink">login</a>
          <a href="top.html" className="btn btn-primary loginLink">main</a>
        </span>
      </nav>

      <div id="registMenu">
        <div>
          <p className="badge bg-secondary">login</p><br />
          <input id="idRegist" placeholder="id" />
        </div>
        <div>
          <p className="badge bg-secondary">password</p><br />
          <input id="passwordRegist" type="password" placeholder="password" />
        </div>
        <div>
          <p className="badge bg-secondary">password check</p><br />
          <input id="passwordRegistCheck" type="password" placeholder="password-check" />
        </div>
        <div>
          <p className="badge bg-secondary">student number</p><br />
          <input placeholder="student-number" />
        </div>
        <div>
          <p className="badge bg-secondary">phone numbe</p><br />
          <input placeholder="phone-number" />
        </div>

        <span>
          <button className="btn btn-success">regist</button>
          <button className="btn btn-outline-danger">cancel</button>
        </span>
      </div>
    </>
  )
}

export default Register;