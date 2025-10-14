<template>
  <div class="user-list">
    <h2>用户列表</h2>
    <el-table :data="users" style="width: 100%" v-loading="loading">
      <el-table-column prop="id" label="ID" width="80"></el-table-column>
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="email" label="邮箱"></el-table-column>
      <el-table-column prop="createdAt" label="创建时间"></el-table-column>
      <el-table-column label="操作" width="150">
        <template slot-scope="scope">
          <el-button size="mini" @click="editUser(scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="deleteUser(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog title="编辑用户" :visible.sync="dialogVisible">
      <el-form :model="currentUser">
        <el-form-item label="姓名">
          <el-input v-model="currentUser.name"></el-input>
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input v-model="currentUser.email"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="saveUser">保存</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { getUsers, updateUser, deleteUser } from '@/api/user'

export default {
  name: 'UserList',
  data() {
    return {
      users: [],
      loading: false,
      dialogVisible: false,
      currentUser: {
        id: null,
        name: '',
        email: ''
      }
    }
  },
  created() {
    this.fetchUsers()
  },
  methods: {
    async fetchUsers() {
      this.loading = true
      try {
        const response = await getUsers()
        this.users = response.data
      } catch (error) {
        this.$message.error('获取用户列表失败')
        console.error(error)
      } finally {
        this.loading = false
      }
    },
    editUser(user) {
      this.currentUser = { ...user }
      this.dialogVisible = true
    },
    async saveUser() {
      try {
        await updateUser(this.currentUser.id, this.currentUser)
        this.$message.success('用户更新成功')
        this.dialogVisible = false
        this.fetchUsers()
      } catch (error) {
        this.$message.error('用户更新失败')
        console.error(error)
      }
    },
    async deleteUser(user) {
      try {
        await this.$confirm('确定要删除该用户吗？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        })
        await deleteUser(user.id)
        this.$message.success('用户删除成功')
        this.fetchUsers()
      } catch (error) {
        if (error !== 'cancel') {
          this.$message.error('用户删除失败')
          console.error(error)
        }
      }
    }
  }
}
</script>

<style scoped>
.user-list {
  padding: 20px;
}
</style>