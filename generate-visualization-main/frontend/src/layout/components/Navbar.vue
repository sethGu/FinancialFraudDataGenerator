<template>
  <div class="navbar">
    <hamburger :is-active="sidebar.opened" class="hamburger-container" @toggleClick="toggleSideBar" />

    <breadcrumb class="breadcrumb-container" />

    <div class="right-menu">
      <el-dropdown class="avatar-container" trigger="click">
        <div class="avatar-wrapper">
<!--          <img :src="avatar+'?imageView2/1/w/80/h/80'" class="user-avatar">-->
          <img :src="url1" class="user-avatar">
<!--          <i class="el-icon-caret-bottom" />-->
        </div>
<!--        <el-dropdown-menu slot="dropdown" class="user-dropdown">-->
<!--          <router-link to="/">-->
<!--            <el-dropdown-item>-->
<!--              Home-->
<!--            </el-dropdown-item>-->
<!--          </router-link>-->
<!--          <a target="_blank" href="https://github.com/PanJiaChen/vue-admin-template/">-->
<!--            <el-dropdown-item>Github</el-dropdown-item>-->
<!--          </a>-->
<!--          <a target="_blank" href="https://panjiachen.github.io/vue-element-admin-site/#/">-->
<!--            <el-dropdown-item>Docs</el-dropdown-item>-->
<!--          </a>-->

<!--          <el-dropdown-item @click.native="logout">-->
<!--            <span style="display:block;">Log out</span>-->
<!--          </el-dropdown-item>-->
<!--          <a target="_blank" @click.prevent="updatePassword">-->
<!--            <el-dropdown-item>Change password</el-dropdown-item>-->
<!--          </a>-->
<!--        </el-dropdown-menu>-->
      </el-dropdown>
    </div>
<!--    <el-dialog width="500px" title="Change Password" :visible.sync="showDialog" append-to-body @close="btnCancel">-->
<!--      <el-form ref="passwordForm" label-width="150px" :model="passwordForm" :rules="rules">-->
<!--        <el-form-item label="Old password" prop="oldPassword">-->
<!--          <el-input v-model="passwordForm.oldPassword" show-password placeholder="Please enter your old password." />-->
<!--        </el-form-item>-->
<!--        <el-form-item label="New password" prop="newPassword">-->
<!--          <el-input v-model="passwordForm.newPassword" show-password placeholder="Please enter your new password." />-->
<!--        </el-form-item>-->
<!--        <el-form-item label="Confirm password" prop="confirmPassword">-->
<!--          <el-input v-model="passwordForm.confirmPassword" show-password placeholder="Please confirm your password." />-->
<!--        </el-form-item>-->
<!--        <el-form-item>-->
<!--          <el-button size="mini" type="primary" @click="btnOK">Confirm</el-button>-->
<!--          <el-button size="mini" @click="btnCancel">Cancel</el-button>-->
<!--        </el-form-item>-->
<!--      </el-form>-->
<!--    </el-dialog>-->
  </div>
</template>

<script>
import { encrypt } from '@/utils/rsaEncrypt'
import { mapGetters } from 'vuex'
import Breadcrumb from '@/components/Breadcrumb'
import Hamburger from '@/components/Hamburger'
import localImage from '@/assets/ff.png'

export default {
  data() {
    return {
      url1: localImage,
      showDialog: false,
      passwordForm: {
        oldPassword: '',
        newPassword: '',
        confirmPassword: ''
      },
      rules: {
        oldPassword: [
          { required: true, message: 'Please enter your old password.', trigger: 'blur' },
          { min: 10, max: 100, message: 'Length must be between 10 and 100 characters.', trigger: 'blur' },
          { pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?<>;:'"{}\[\]\\/|`~+=_-])[A-Za-z\d!@#$%^&*(),.?<>;:'"{}\[\]\\/|`~+=_-]{10,100}$/, message: 'Must include uppercase and lowercase letters, numbers, and special characters.', trigger: 'blur' }
        ],
        newPassword: [
          { required: true, message: 'Please enter your new password.', trigger: 'blur' },
          { min: 10, max: 100, message: 'Length must be between 10 and 100 characters.', trigger: 'blur' },
          { pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?<>;:'"{}\[\]\\/|`~+=_-])[A-Za-z\d!@#$%^&*(),.?<>;:'"{}\[\]\\/|`~+=_-]{10,100}$/, message: 'Must contain uppercase and lowercase letters, numbers, and special characters.', trigger: 'blur' }
        ],
        confirmPassword: [
          { required: true, message: 'Please enter your new password again.', trigger: 'blur' },
          { min: 10, max: 100, message: 'Length must be between 6 and 16 characters.', trigger: 'blur' },
          { pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?<>;:'"{}\[\]\\/|`~+=_-])[A-Za-z\d!@#$%^&*(),.?<>;:'"{}\[\]\\/|`~+=_-]{10,100}$/, message: 'Must contain uppercase and lowercase letters, numbers, and special characters.', trigger: 'blur' },
          {
            validator: (rule, value, callback) => {
              if (value !== this.passwordForm.newPassword) {
                callback(new Error('The two passwords do not match!'))
              } else {
                callback()
              }
            },
            trigger: 'blur'
          }
        ]
      }
    }
  },
  components: {
    Breadcrumb,
    Hamburger
  },
  computed: {
    ...mapGetters([
      'sidebar',
      'avatar'
    ])
  },
  methods: {
    toggleSideBar() {
      this.$store.dispatch('app/toggleSideBar')
    },
    async logout() {
      await this.$store.dispatch('user/logout')
      this.$router.push(`/login?redirect=${this.$route.fullPath}`)
    },
    updatePassword() {
      this.showDialog = true
    },
    btnOK() {
      this.$refs.passwordForm.validate(async valid => {
        if (valid) {
          try {
            this.passwordForm.oldPassword = encrypt(this.passwordForm.oldPassword)
            this.passwordForm.newPassword = encrypt(this.passwordForm.newPassword)
            this.passwordForm.confirmPassword = encrypt(this.passwordForm.confirmPassword)

            await this.$store.dispatch('user/updatePassword', this.passwordForm)
            this.$message.success('Password changed successfully.')
            this.btnCancel()
            this.logout()
          } catch (error) {
            this.$message.error('Incorrect old password!')
            this.$refs.passwordForm.resetFields()
          }
        }
      })
    },
    btnCancel() {
      this.$refs.passwordForm.resetFields()
      this.showDialog = false
    }
  }
}
</script>

<style lang="scss" scoped>
.navbar {
  height: 50px;
  overflow: hidden;
  position: relative;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0,21,41,.08);

  .hamburger-container {
    line-height: 46px;
    height: 100%;
    float: left;
    cursor: pointer;
    transition: background .3s;
    -webkit-tap-highlight-color:transparent;

    &:hover {
      background: rgba(0, 0, 0, .025)
    }
  }

  .breadcrumb-container {
    float: left;
  }

  .right-menu {
    float: right;
    height: 100%;
    line-height: 50px;

    &:focus {
      outline: none;
    }

    .right-menu-item {
      display: inline-block;
      padding: 0 8px;
      height: 100%;
      font-size: 18px;
      color: #5a5e66;
      vertical-align: text-bottom;

      &.hover-effect {
        cursor: pointer;
        transition: background .3s;

        &:hover {
          background: rgba(0, 0, 0, .025)
        }
      }
    }

    .avatar-container {
      margin-right: 30px;

      .avatar-wrapper {
        margin-top: 5px;
        position: relative;

        .user-avatar {
          cursor: pointer;
          width: 40px;
          height: 40px;
          border-radius: 10px;
        }

        .el-icon-caret-bottom {
          cursor: pointer;
          position: absolute;
          right: -20px;
          top: 25px;
          font-size: 12px;
        }
      }
    }
  }
}
</style>
