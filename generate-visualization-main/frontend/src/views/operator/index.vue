<template>
  <div class="app-container">
    <div class="operator-header">
      <div id="number">
        用户数量
        <el-input-number v-model="num" :min="1" label="" @change="handleChange" />
      </div>

      <div class="operatorGe-btn">
        <el-button type="primary" round @click="create()">数据生成</el-button>
        <el-button round @click="reset()">参数重置</el-button>
        <el-button round @click="download()">数据下载</el-button>
        <el-button type="danger" round @click="deleteData()">数据删除</el-button>
      </div>
    </div>

    <div class="chart-container">
      <div id="chartSankey" class="chart" style="height:500px;width:60%;padding: 5px;float: left;overflow: hidden;margin-top: 15px;margin-bottom: 15px;" />
      <div id="chartBing" class="chart" style="height:500px;width:40%;padding: 5px;float: left;overflow: hidden; margin-top: 15px;margin-bottom: 15px;" />

      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>用户运营商数据示例</span>
        </div>
        <div class="filter-container">
          <el-input v-model="listQuery.original_id" placeholder="原始id" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
          <el-input v-model="listQuery.contactor" placeholder="触点" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
          <el-input v-model="listQuery.mobile_phone_brand" placeholder="手机品牌" clearable class="filter-item" style="width: 130px" />
          <el-select v-model="listQuery.sort" style="width: 140px" class="filter-item" @change="handleFilter">
            <el-option v-for="item in sortOptions" :key="item.key" :label="item.label" :value="item.key" />
          </el-select>
          <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
            搜索
          </el-button>
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
          <el-table-column label="原始id" width="400px" align="center">
            <template slot-scope="{row}">
              <span>{{ row.original_id }}</span>
            </template>
          </el-table-column>
          <el-table-column label="触点" min-width="50px">
            <template slot-scope="{row}">
              <span class="link-type">{{ row.contactor }}</span>
            </template>
          </el-table-column>
          <el-table-column label="终端类型" min-width="50px">
            <template slot-scope="{row}">
              <span class="link-type">{{ row.terminal_type }}</span>
            </template>
          </el-table-column>
          <el-table-column label="手机品牌" width="110px" align="center">
            <template slot-scope="{row}">
              <span>{{ row.mobile_phone_brand }}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作系统" width="110px" align="center">
            <template slot-scope="{row}">
              <span>{{ row.mobile_operating_system }}</span>
            </template>
          </el-table-column>
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
            <el-descriptions v-if="operator_data" class="margin-top" title="" :column="3" border :content-style="CS" :label-style="LS ">
              <el-descriptions-item label="原始ID">
                {{ operator_data.operators_example_list[table_id].original_id }}
              </el-descriptions-item>
              <el-descriptions-item label="触点">
                {{ operator_data.operators_example_list[table_id].contactor }}
              </el-descriptions-item>
              <el-descriptions-item label="触点ID">
                {{ operator_data.operators_example_list[table_id].contactor_id }}
              </el-descriptions-item>
              <el-descriptions-item label="手机品牌">
                {{ operator_data.operators_example_list[table_id].mobile_phone_brand }}
              </el-descriptions-item>
              <el-descriptions-item label="手机操作系统">
                {{ operator_data.operators_example_list[table_id].mobile_operating_system }}
              </el-descriptions-item>
              <el-descriptions-item label="pv">
                {{ operator_data.operators_example_list[table_id].pv }}
              </el-descriptions-item>
              <el-descriptions-item label="终端类型">
                {{ operator_data.operators_example_list[table_id].terminal_type }}
              </el-descriptions-item>
              <el-descriptions-item label="视频网站">
                {{ operator_data.operators_example_list[table_id].video_website }}
              </el-descriptions-item>
              <el-descriptions-item label="购物网站">
                {{ operator_data.operators_example_list[table_id].shopping_website }}
              </el-descriptions-item>
              <el-descriptions-item label="海淘购物渠道">
                {{ operator_data.operators_example_list[table_id].overseas_taobao_shopping_channel }}
              </el-descriptions-item>
              <el-descriptions-item label="汽车网站">
                {{ operator_data.operators_example_list[table_id].automotive_website }}
              </el-descriptions-item>
              <el-descriptions-item label="房产网站">
                {{ operator_data.operators_example_list[table_id].real_estate_website }}
              </el-descriptions-item>
              <el-descriptions-item label="旅游网站">
                {{ operator_data.operators_example_list[table_id].travel_website }}
              </el-descriptions-item>
              <el-descriptions-item label="当月内用户日最高主叫通话次数">
                {{ operator_data.operators_example_list[table_id].highest_calling }}
              </el-descriptions-item>
              <el-descriptions-item label="当月与该号码通话的对端所属城市数量">
                {{ operator_data.operators_example_list[table_id].city_number }}
              </el-descriptions-item>
              <el-descriptions-item label="工作日白天主叫通话次数">
                {{ operator_data.operators_example_list[table_id].day_calling }}
              </el-descriptions-item>
              <el-descriptions-item label="工作日夜间通话天数">
                {{ operator_data.operators_example_list[table_id].night_calling }}
              </el-descriptions-item>
              <el-descriptions-item label="近三月月均主叫通话次数" >
                {{ operator_data.operators_example_list[table_id].three_month_calling }}
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
import { operatorDataInit, generateOperator, operatorRecreateTable } from '@/api/operator'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import waves from '@/directive/waves'
import { fetchList } from '@/api/operator' // waves directive

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
      num: 1,
      rules: {
        type: [{ required: true, message: 'type is required', trigger: 'change' }],
        timestamp: [{ type: 'date', required: true, message: 'timestamp is required', trigger: 'change' }],
        title: [{ required: true, message: 'title is required', trigger: 'blur' }],
        num: [
          { required: true, message: '请输入企业数量', trigger: 'blur' }
        ]
      },
      operator_data: '',
      // 描述列表样式===========开始=============
      CS: {
        'text-align': 'center', // 文本居中
        'min-width': '2500px', // 最小宽度
        'word-break': 'break-all' // 过长时自动换行
      },
      LS: {
        'color': '#000',
        'text-align': 'center',
        'font-weight': '600',
        'height': '40px',
        'background-color': 'rgba(255, 97, 2, 0.1)',
        'min-width': '100px',
        'word-break': 'break-all'
      }
      // 描述列表样式===========结束=============
    }
  },
  created() {
    this.operatorDataInit()
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
    operatorDataInit() {
      operatorDataInit().then((response) => {
        console.log(response)
        this.operator_data = response.data
        this.showBing()
        this.showSankey()
      })
    },
    reset() {
      // console.log("This is num:",this.num);
      this.num = 1
    },
    download() {
      window.location.href = '/api_operator/operator/download/'
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
        operatorRecreateTable().then(response => {
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
        const loadingInstanceSankey = Loading.service({ // 启动loading服务
          target: document.querySelector('#chartSankey'),
          fullscreen: false
        })
        const loadingInstanceBing = Loading.service({ // 启动loading服务
          target: document.querySelector('#chartBing'),
          fullscreen: false
        })
        // 请求数据生成
        generateOperator(this.num).then(response => {
          console.log(response)
          loadingInstanceSankey.close()
          loadingInstanceBing.close()
          this.showBing()
          this.showSankey()
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
    showSankey() {
      if (this.operator_data) {
        this.chart = echarts.init(document.getElementById('chartSankey'))
        var option = {
          backgroundColor: '#fff',
          title: {
            text: '运营商网站统计',
            left: 'center'
          },
          series: [
            {
              type: 'sankey',
              layout: 'none',
              emphasis: {
                focus: 'adjacency'
              },
              // type: 'sankey',
              // left: 50.0,
              // top: 20.0,
              // right: 150.0,
              // bottom: 25.0,
              data: this.operator_data.website_type.data_info,
              links: this.operator_data.website_type.data_link
              // lineStyle: {
              //   color: 'source',
              //   curveness: 0.5
              // },
              // itemStyle: {
              //   color: '#1f77b4',
              //   borderColor: '#1f77b4'
              // },
              // label: {
              //   color: 'rgba(0,0,0,0.7)',
              //   fontFamily: 'Arial',
              //   fontSize: 10
              // }
            }
          ],
          tooltip: {
            trigger: 'item'
          }
        }
        this.chart.setOption(option)
      }
    },
    showBing() {
      if (this.operator_data) {
        this.chart = echarts.init(document.getElementById('chartBing'))
        var option = {
          title: {
            text: '手机品牌统计',
            // subtext: 'Fake Data',
            left: 'center'
          },
          tooltip: {
            trigger: 'item'
          },
          legend: {
            type: 'scroll',
            orient: 'horizontal',
            left: 'center',
            top: 30
          },
          series: [
            {
              name: '数量',
              type: 'pie',
              radius: '50%',
              data: this.operator_data.phone_type,
              // data: [
              //   { value: 1048, name: 'Search Engine' },
              //   { value: 735, name: 'Direct' },
              //   { value: 580, name: 'Email' },
              //   { value: 484, name: 'Union Ads' },
              //   { value: 300, name: 'Video Ads' }
              // ],
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
.operator-header{
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
.long-descriptions{
  min-width: 1000px;
}
.operatorGe-btn{
  display: inline-block;
}
.chart-container{
  width: 100%;
  margin-top: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
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
