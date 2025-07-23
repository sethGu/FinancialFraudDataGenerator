<template>
  <div class="login-container">
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form" auto-complete="on" label-position="left">

      <div class="title-container">
        <h3 class="title">Financial Risk Simulation Software for Payment Systems</h3>
      </div>

      <el-form-item prop="username">
        <span class="svg-container">
          <svg-icon icon-class="user" />
        </span>
        <el-input
          ref="username"
          v-model="loginForm.username"
          placeholder="Enter username"
          name="username"
          type="text"
          tabindex="1"
          auto-complete="off"
        />
      </el-form-item>

      <el-form-item prop="password">
        <span class="svg-container">
          <svg-icon icon-class="password" />
        </span>
        <el-input
          :key="passwordType"
          ref="password"
          v-model="loginForm.password"
          :type="passwordType"
          placeholder="Enter password"
          name="password"
          tabindex="2"
          auto-complete="off"
          @keyup.enter.native="handleLogin"
        />
        <span class="show-pwd" @click="showPwd">
          <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
        </span>
      </el-form-item>

      <el-button :loading="loading" type="primary" style="width:100%;margin-bottom:30px;" @click.native.prevent="handleLogin">Login</el-button>

    </el-form>
    <!--    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320">-->
    <!--      <path-->
    <!--        fill="#06397E"-->
    <!--        fill-opacity="1"-->
    <!--        d="M0,192L60,176C120,160,240,128,360,122.7C480,117,600,139,720,160C840,181,960,203,1080,202.7C1200,203,1320,181,1380,170.7L1440,160L1440,320L1380,320C1320,320,1200,320,1080,320C960,320,840,320,720,320C600,320,480,320,360,320C240,320,120,320,60,320L0,320Z"-->
    <!--      />-->
    <!--    </svg>-->

  </div>
</template>

<script>
import { validUsername } from '@/utils/validate'
import { encrypt } from '@/utils/rsaEncrypt'
export default {
  name: 'Login',
  data() {
    const validateUsername = (rule, value, callback) => {
      // 详见validate.js
      if (!validUsername(value)) {
        callback(new Error('Please enter a valid username!'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      // 密码规格：10-100个字符，包含大小写字母、数字、特殊字符
      if (!/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?<>;:'"{}\[\]\\/|`~+=_-])[A-Za-z\d!@#$%^&*(),.?<>;:'"{}\[\]\\/|`~+=_-]{10,100}$/.test(value)) {
        callback(new Error('Must include uppercase and lowercase letters, numbers, and special characters.'))
      } else {
        callback()
      }
    }
    return {
      // 用户账号密码
      loginForm: {
        username: '',
        password: ''
      },
      // 登陆规则，详见validator
      loginRules: {
        username: [{ required: true, trigger: 'blur', validator: validateUsername }],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }]
      },
      loading: false,
      passwordType: 'password',
      redirect: undefined
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },
  methods: {
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    // 点击登陆按钮触发的函数
    handleLogin() {
      // loginForm表单验证，详见loginRules
      this.$refs.loginForm.validate(valid => {
        // 验证成功
        if (valid) {
          this.loading = true
          // 调用src/store/modules/user.js中login方法
          // 密码加密
          console.log('loginForm before encryption:', this.loginForm)
          console.log('loginForm:', this.loginForm)
          this.loginForm.password = encrypt(this.loginForm.password)
          console.log('loginForm:', this.loginForm)
          this.$store.dispatch('user/login', this.loginForm)
            .then(() => { // 登陆成功
              // 路由到dashboard
              this.$router.push({ path: this.redirect || '/' })
              this.loading = false
            }).catch(() => { // 异常
              this.loading = false
              this.$refs.loginForm.clearValidate()
              this.$refs.loginForm.resetFields()
            })
        } else {
          console.log('Login failed!')
          return false
        }
      })
    }
  }
}
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg:#283443;
$light_gray:#fff;
$cursor: #fff;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.login-container {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      height: 47px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }
}
</style>

<style lang="scss" scoped>
$bg:#2d3a4b;
$dark_gray:#889aa4;
$light_gray:#eee;
$shu-blue:#06397E;
$CU-red:#DD2C34;
$CU-white:#F5F5F5;

//.el-button{
//  background-color: $shu-blue;
//  border-color: $shu-blue;
//}

.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  //background: rgb(221,44,52);
  //background: linear-gradient(90deg, rgba(221,44,52,1) 0%, rgba(0,72,137,1) 35%, rgba(2,129,136,1) 100%);
  overflow: hidden;

  .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
  }

  .tips {
    font-size: 14px;
    color: #fff;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }
}
</style>
