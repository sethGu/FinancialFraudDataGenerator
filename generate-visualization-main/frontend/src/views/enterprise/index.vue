<template>
  <div class="app-container">
    <div class="enterprise-header">
      <div id="number">
        工商企业数量
        <el-input-number v-model="num" :min="1" label="" @change="handleChange" />
      </div>

      <div class="enterpriseGe-btn">
        <el-button type="primary" round @click="create()">数据生成</el-button>
        <el-button round @click="reset()">参数重置</el-button>
        <el-button round @click="download()">数据下载</el-button>
        <el-button type="danger" round @click="deleteData()">数据删除</el-button>
      </div>
    </div>
    <div class="chart-container">
      <div id="chartFunnel" class="chart" style="height:500px;width:50%;padding: 5px; float: left;overflow: hidden; margin-top: 15px;margin-bottom: 15px;" />
      <div id="chartBing" class="chart" style="height:500px;width:50%;padding: 5px;float: left;overflow: hidden; margin-top: 15px;margin-bottom: 15px;" />

      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>工商企业数据示例</span>
        </div>
        <div class="filter-container">
          <el-input v-model="listQuery.name" placeholder="公司名" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
          <el-input v-model="listQuery.locate" placeholder="地名" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
          <el-select v-model="listQuery.type" placeholder="公司类型" clearable class="filter-item" style="width: 130px">
            <el-option v-for="item in enterpriseTypeOptions" :key="item" :label="item" :value="item" />
          </el-select>
          <el-select v-model="listQuery.sort" style="width: 140px" class="filter-item" @change="handleFilter">
            <el-option v-for="item in sortOptions" :key="item.key" :label="item.label" :value="item.key" />
          </el-select>
          <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
            搜索
          </el-button>
          <!--          <el-button v-waves :loading="downloadLoading" class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">-->
          <!--            导出-->
          <!--          </el-button>-->

        </div>
        <el-table
          :key="tableKey"
          v-loading="listLoading"
          :data="list"
          border
          fit
          highlight-current-row
          style="width: 100%;"
          @sort-change="sortChange"
        >
          <el-table-column label="ID" prop="id" sortable="custom" align="center" width="80" :class-name="getSortClass('id')">
            <template slot-scope="{row}">
              <span>{{ row.id }}</span>
            </template>
          </el-table-column>
          <el-table-column label="社会信用代码" width="200px" align="center">
            <template slot-scope="{row}">
              <span>{{ row.socialid }}</span>
            </template>
          </el-table-column>
          <el-table-column label="公司名" min-width="150px">
            <template slot-scope="{row}">
              <span class="link-type">{{ row.name }}</span>
            </template>
          </el-table-column>
          <el-table-column label="法人" width="110px" align="center">
            <template slot-scope="{row}">
              <span>{{ row.represent }}</span>
            </template>
          </el-table-column>
          <!--          <el-table-column label="详细信息" align="center" width="230" class-name="small-padding fixed-width">-->
          <!--            <template slot-scope="{row}">-->
          <!--              <el-button type="primary" size="mini" @click="showdetail(row)">-->
          <!--                查看-->
          <!--              </el-button>-->
          <!--            </template>-->
          <!--          </el-table-column>-->
          <el-table-column
            align="center"
            label="详细信息"
            width="100"
          >
            <template slot-scope="scope">
              <el-button type="primary" size="small" @click="handleClick(scope.row)">查看</el-button>
            </template>
          </el-table-column>
        </el-table>

        <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
        <el-dialog title="企业详细信息" :visible.sync="dialogFormVisible">
          <div id="desList">
            <el-descriptions v-if="enterprise_data" prop="id" class="margin-top" title="" :column="3" border :content-style="CS" :label-style="LS ">
              <el-descriptions-item label="注册号">
                <!-- 972761407486200 -->

                {{ enterprise_data.enterprises_example_list[table_id].registerid }}
              </el-descriptions-item>
              <el-descriptions-item label="法定代表人">
                <!-- 暴瑗 -->
                {{ enterprise_data.enterprises_example_list[table_id].represent }}
              </el-descriptions-item>
              <el-descriptions-item label="类型">
                <!-- 两合公司 -->
                {{ enterprise_data.enterprises_example_list[table_id].type }}
              </el-descriptions-item>
              <el-descriptions-item label="成立日期">
                <!-- 20021009 -->
                {{ enterprise_data.enterprises_example_list[table_id].builttime }}
              </el-descriptions-item>
              <el-descriptions-item label="注册资本(万元)">
                <!-- 1062.27 -->
                {{ enterprise_data.enterprises_example_list[table_id].regamount }}
              </el-descriptions-item>
              <el-descriptions-item label="核准日期">
                <!-- 20191021 -->
                {{ enterprise_data.enterprises_example_list[table_id].checktime }}
              </el-descriptions-item>
              <el-descriptions-item label="登记机关">
                <!-- 洛阳市市场监督管理局 -->
                {{ enterprise_data.enterprises_example_list[table_id].reglocate }}
              </el-descriptions-item>
              <el-descriptions-item label="登记状态">
                <!-- 存续 -->
                {{ enterprise_data.enterprises_example_list[table_id].state }}
              </el-descriptions-item>
              <el-descriptions-item label="住所">
                <!-- 洛阳市 -->
                {{ enterprise_data.enterprises_example_list[table_id].locate }}
              </el-descriptions-item>
              <el-descriptions-item label="经营范围">
                {{ enterprise_data.enterprises_example_list[table_id].busscope }}
                <!-- 废金属处理设施，纺织废料处理设施，皮革废料及处理设施，化工废料及处理设施，废气处理设施，水、污水处理设施，废料回收再利用 -->
              </el-descriptions-item>
            </el-descriptions>
          </div>
        </el-dialog>

      </el-card>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts'
import { Loading } from 'element-ui'
import { enterpriseDataInit, enterpriseRecreateTable, fetchList, generateEnterprise } from '@/api/enterprise'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import waves from '@/directive/waves'

export default {
  components: { Pagination },
  directives: { waves },
  data() {
    return {
      table_id: 0,
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        name: undefined,
        locate: undefined,
        type: undefined,
        sort: '+id'
      },
      sortOptions: [{ label: 'ID Ascending', key: '+id' }, { label: 'ID Descending', key: '-id' }],
      dialogFormVisible: false,
      dialogStatus: '',
      dialogPvVisible: false,
      pvData: [],
      downloadLoading: false,
      enterprise_data: '',
      num: 1,
      rules: {
        type: [{ required: true, message: 'type is required', trigger: 'change' }],
        timestamp: [{ type: 'date', required: true, message: 'timestamp is required', trigger: 'change' }],
        title: [{ required: true, message: 'title is required', trigger: 'blur' }],
        num: [
          { required: true, message: '请输入企业数量', trigger: 'blur' }
        ]
      },
      enterpriseTypeOptions: ['两合公司', '有限责任公司', '无限责任公司', '股份两合公司', '股份有限公司'],
      // 描述列表样式===========开始=============
      CS: {
        'text-align': 'center', // 文本居中
        'min-width': '250px', // 最小宽度
        'word-break': 'break-all' // 过长时自动换行
      },
      LS: {
        'color': '#000',
        'text-align': 'center',
        'font-weight': '600',
        'height': '40px',
        'background-color': 'rgba(255, 97, 2, 0.1)',
        'min-width': '100px',
        'word-break': 'keep-all'
      }
      // 描述列表样式===========结束=============
    }
  },
  created() {
    this.enterpriseDataInit()
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      fetchList(this.listQuery).then(response => {
        console.log('fetchList!', response)
        this.list = response.data.items
        this.total = response.data.total
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    sortChange(data) {
      const { prop, order } = data
      if (prop === 'id') {
        this.sortByID(order)
      }
    },
    sortByID(order) {
      if (order === 'ascending') {
        this.listQuery.sort = '+id'
      } else {
        this.listQuery.sort = '-id'
      }
      this.handleFilter()
    },
    handleClick(row) {
      console.log(row.id)
      this.table_id = row.id - 1
      this.dialogFormVisible = true
    },
    getSortClass: function(key) {
      const sort = this.listQuery.sort
      return sort === `+${key}` ? 'ascending' : 'descending'
    },
    handleChange(value) {
      this.num = value
    },
    enterpriseDataInit() {
      enterpriseDataInit().then((response) => {
        this.enterprise_data = response.data
        this.showBing()
        this.showFunnel()
      })
    },
    reset() {
      // console.log("This is num:",this.num);
      this.num = 1
    },
    download() {
      window.location.href = '/api_enterprise/enterprise/download/'
    },
    deleteData() {
      this.$confirm('是否删除数据?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'success',
          message: '删除数据成功!'
        })
        enterpriseRecreateTable().then(response => {
          // 自动刷新
          this.$router.go(0)
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消操作'
        })
      })
    },
    create() {
      this.$confirm('是否生成数据?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'success',
          message: '生成数据成功!'
        })
        const loadingInstanceFunnel = Loading.service({ // 启动loading服务
          target: document.querySelector('#chartFunnel'),
          fullscreen: false
        })
        const loadingInstanceBing = Loading.service({ // 启动loading服务
          target: document.querySelector('#chartBing'),
          fullscreen: false
        })
        // 请求数据生成
        generateEnterprise(this.num).then(response => {
          console.log(response)
          loadingInstanceFunnel.close()
          loadingInstanceBing.close()
          this.showBing()
          this.showFunnel()
        })
        // 自动刷新
        this.$router.go(0)
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消操作'
        })
      })
    },
    showFunnel() {
      if (this.enterprise_data) {
        this.chart = echarts.init(document.getElementById('chartFunnel'))
        var option = {
          title: {
            text: '企\n业\n类\n型\n统\n计',
            top: 'center'
          },
          tooltip: {
            formatter: '{a} <br/>{b} : {c}'
          },
          toolbox: {
            orient: 'horizontal',
            left: 'right',
            feature: {
              dataView: { readOnly: false },
              restore: {},
              saveAsImage: {}
            }
          },
          legend: {
            orient: 'horizontal',
            left: 'center',
            top: '5%',
            data: this.enterprise_data.type_info.data_type
          },
          series: [
            {
              name: '企业数量',
              type: 'funnel',
              width: '35%',
              height: '40%',
              left: '5%',
              top: '55%',
              data: this.enterprise_data.type_info.data_type_info
            },
            {
              name: '企业数量',
              type: 'funnel',
              width: '35%',
              height: '40%',
              left: '5%',
              top: '15%',
              sort: 'ascending',
              data: this.enterprise_data.type_info.data_type_info
            },
            {
              name: '企业数量',
              type: 'funnel',
              width: '35%',
              height: '40%',
              left: '55%',
              top: '15%',
              label: {
                position: 'left'
              },
              data: this.enterprise_data.type_info.data_type_info
            },
            {
              name: '企业数量',
              type: 'funnel',
              width: '35%',
              height: '40%',
              left: '55%',
              top: '55%',
              sort: 'ascending',
              label: {
                position: 'left'
              },
              data: this.enterprise_data.type_info.data_type_info
            }
          ]
        }
        this.chart.setOption(option)
      }
    },
    showBing() {
      if (this.enterprise_data) {
        this.chart = echarts.init(document.getElementById('chartBing'))
        var option = {
          title: {
            text: '企\n业\n注\n册\n区\n域\n统\n计',
            top: 'center'
          },
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
          },
          legend: {
            type: 'scroll',
            orient: 'vertical',
            right: 10,
            top: 20,
            bottom: 20,
            data: this.enterprise_data.area_info.data_area
          },
          series: [
            {
              name: '企业数量数量',
              type: 'pie',
              radius: '50%',
              center: ['43%', '50%'],
              data: this.enterprise_data.area_info.data_info,
              emphasis: {
                itemStyle: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
        }
        this.chart.setOption(option)
      }
    }

  }
}
</script>

<style scoped>
.enterprise-header{
  position: relative;
  text-align: center;
  margin: 10px auto;
  width: 100%;
  height: 200px;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5), 0 0 6px rgba(0, 0, 0, .04);
}
#number{
  padding: 50px 0 30px 0;
}
.el-input-number{
  margin-left: 10px;
}
.enterpriseGe-btn{
  display: inline-block;
}
.chart-container{
  width: 100%;
  margin-top: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
}
.chart{
  height: 500px;
  width: 50%;
  padding: 5px;
  float: left;
  overflow: hidden;
  margin: 15px 0;
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both
}
.box-card {
  margin:1% auto;
}
/deep/ .el-descriptions .is-bordered{
  table-layout: fixed;
}
</style>
