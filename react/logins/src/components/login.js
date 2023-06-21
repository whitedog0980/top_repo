import './beforeMig/css.css'

function Login () {
  return (
    <>
      <nav className="navigate">
        <span id="loginSpan">
          <a href="top.html" className="btn btn-primary loginLink">main</a>
          <a href="regist.html" className="btn btn-light loginLink">register</a>
        </span>
      </nav>

      <div id="loginMenu">
        <div>
          <p className="badge bg-secondary">login</p><br />
          <input id="loginInput" type="id" placeholder="id" />
        </div>
        <div>
          <p className="badge bg-secondary">password</p><br />
          <input id="passwordInput" type="password" placeholder="password" />
        </div>
        <button id="loginBtn" className="btn btn-success">login</button>
      </div>
    </>
  )
}

export default Login;