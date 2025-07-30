<template>
  <div class="app-container">
    <div class="gamb-header">
      <el-form ref="form" :model="form" :rules="rules" :inline="true" label-width="200px">
        <div class="shortLong" />
        <el-form-item id="userAmount" label="Number of users">
          <el-input-number
            v-model="userAmount"
            controls-position="right"
            :min="20"
          />
        </el-form-item>
        <el-form-item label="Violative users count">
          <el-input-number v-model="form.user" :min="30" label="Description text" />
        </el-form-item>
        <el-form-item label="Nighttime transaction ratio">
          <el-input-number v-model="form.personalTrans" :precision="1" :min="0.1" :step="0.1" :max="1" />
        </el-form-item>
        <el-form-item id="storeAmount" label="Number of merchants">
          <el-input-number v-model="storeAmount" controls-position="right" :min="10" />
        </el-form-item>
        <el-form-item label="Violative merchants count">
          <el-input-number v-model="form.store" :min="1" label="Description text" />
        </el-form-item>
        <el-form-item label="Merchant low-range ratio">
          <el-input-number v-model="form.storeLow" :precision="1" :min="0.1" :step="0.1" :max="1" />
        </el-form-item>

        <el-form-item label="Generation cycle">
          <el-popover
            placement="top-start"
            title="Tip"
            width="200"
            trigger="hover"
            content="Select number of days"
          >
            <el-input-number
              slot="reference"
              v-model="form.duration"
              controls-position="right"
              :min="1"
              :disabled="btnDisabled"
            />
          </el-popover>
        </el-form-item>
        <el-form-item label="Select time" prop="startDate">
          <el-date-picker
            v-model="form.startDate"
            style="width: 190px"
            type="date"
            placeholder="Select start date"
            format="yyyy-MM-dd"
            value-format="yyyyMMdd"
            :picker-options="pickerOptions"
            :disabled="btnDisabled"
          />
        </el-form-item>
        <el-form-item label="Merchant mid-range ratio">
          <el-input-number v-model="form.storeMiddle" :precision="1" :min="0.1" :step="0.1" :max="1" />
        </el-form-item>

        <el-form-item label="Operating time ratio">
          <el-input-number v-model="form.isOpenTime" :precision="1" :min="0.1" :step="0.1" :max="1" />
        </el-form-item>
        <el-form-item label="Gambling user ratio">
          <el-input-number v-model="form.gambleUser" :precision="1" :min="0.1" :step="0.1" :max="1" />
        </el-form-item>
        <el-form-item label="Merchant high-range ratio">
          <el-input-number v-model="form.storeHigh" :precision="1" :min="0.1" :step="0.1" :max="1" />
        </el-form-item>
        <!-- <div class="selectTime"> -->
        <el-checkbox-group v-model="checkList" class="checkData">
          <el-checkbox label="Normal transaction data generation" border size="big" @change="conC" />
        </el-checkbox-group>
        <!-- </div> -->
        <div class="gambleGebtn">
          <el-button type="primary" round size="large" @click="create()">Data generation</el-button>
          <el-button type="default" round size="large" @click="reset()">Parameter reset</el-button>
          <el-button type="default" round size="large" @click="download()">Data download</el-button>
          <el-button type="danger" round size="large" @click="deleteData()">Data deletion</el-button>
        </div>
      </el-form>
    </div>
    <div class="chart-container" style="width: 25%;">
      <div id="chartCard" class="chart" style="height:200px;width:100%;padding: 5px;" />
      <div id="chartGambling" class="chart" style="height:200px;width:100%;padding: 5px;" />
    </div>
    <div class="chart-container" style="width: 75%;">
      <div id="chartStoreBig" class="chart" style="height:400px;width:100%;padding: 5px;" />
    </div>
    <div class="chart-container" style="width: 25%;">
      <div id="chartUserAge" class="chart" style="height:500px;width:100%;padding: 5px;" />
    </div>
    <!-- <div class="chart-container" style="width: 37.5%;">
      <div id="chartUserJob" class="chart" style="height:400px;width:100%;padding: 5px;" />
    </div> -->
    <div class="chart-container" style="width: 75%;">
      <div id="chartFraud" class="chart" style="height:250px;width:100%;padding: 5px;" />
      <div id="chartConsume" class="chart" style="height:250px;width:100%;padding: 5px;" />
      <!-- <div id="chartTrans" class="chart" style="height:250px;width:100%;padding: 5px;" /> -->
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts'
import { mapGetters } from 'vuex'
import { Loading } from 'element-ui'
import { logChange } from '@/api/logs'

export default {
  data() {
    return {
      btnDisabled: false,
      userAmount: 50,
      storeAmount: 20,
      is_con: false,
      is_tran: false,
      checkList: [],
      store: {
        totaldata: [],
        totalvalue: [],
        parantClassdata: [],
        parantClassvalue: [],
        childClassdata: [],
        childClassvalue: [],
        dictClass: []
      },
      cardsOwnerType: [],
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now()
        }
      },
      rules: {
        startDate: [
          { required: true, message: 'Please select a date.', trigger: 'blur' }
        ]
      },
      form: {
        store: 10,
        user: 30,
        startDate: '20221001',
        duration: 30,
        storeLow: 0.3, // low_rank_store_ratio
        storeMiddle: 0.6, // middle_rank_store_ratio
        storeHigh: 0.1, // high_rank_store_ratio
        isOpenTime: 0.1, // is_in_opening_time
        gambleUser: 0.2, // gambling_user_ratio
        personalTrans: 0.1// personal_trans_time_ratio
      }
    }
  },
  computed: {
    ...mapGetters([
      'gambling_user_data',
      'gambling_store_data',
      'gambling_card_data',
      'gambling_consume_data',
      'gambling_transfer_data',
      'gambling_date_data',
      'gambling_data'
    ])
  },
  beforeCreate() {
    this.$store.dispatch('gambling/durationSetGambling').then(() => {
      this.form.startDate = this.$store.state.gambling.gambling_date_data.startDate
      this.form.duration = this.$store.state.gambling.gambling_date_data.duration
    })
  },
  created() {
    this.init()
  },
  methods: {
    conC(value) {
      this.is_con = value
      this.is_tran = value
    },
    tranC(value) {
      this.is_tran = value
    },
    dispatchCon() {
      if (this.is_con) {
        console.log('consumeGenerate')
        return this.$store.dispatch('gambling/consumeGenerateGambling', { date: this.form.startDate, duration: this.form.duration })
      } else {
        console.log('consumeInit')
        return this.$store.dispatch('gambling/consumeInitGambling', { date: this.form.startDate, duration: this.form.duration })
      }
    },
    dispatchTran() {
      if (this.is_tran) {
        console.log('transferGenerate')
        return this.$store.dispatch('gambling/transferGenerateGambling', { date: this.form.startDate, duration: this.form.duration })
      } else {
        console.log('transferInit')
        return this.$store.dispatch('gambling/transferInitGambling', { date: this.form.startDate, duration: this.form.duration })
      }
    },
    reset() {
      this.userAmount = 50
      this.storeAmount = 20
      this.is_con = false
      this.is_tran = false
      this.checkList.pop()
      this.checkList.pop()
      this.form.startDate = '20221001'
      this.form.duration = 30
      this.form.store = 10
      this.form.user = 30
      this.form.gambleUser = 0.2
      this.form.isOpenTime = 0.1
      this.form.personalTrans = 0.1
      this.form.storeHigh = 0.1
      this.form.storeMiddle = 0.6
      this.form.storeLow = 0.3
      logChange({
        change: 'GamblingTrans reset',
        result: 'success'
      }).then(response => {
        console.log('Log recorded successfully', response.data)
      }).catch(error => {
        console.error('Log recording failed', error)
      })
    },
    deleteData() {
      this.$confirm('Do you want to delete the data?', 'Tip', {
        confirmButtonText: 'Yes',
        cancelButtonText: 'No',
        type: 'warning'
      }).then(() => {
        logChange({
          change: 'GamblingTrans deleteData',
          result: 'success'
        }).then(response => {
          console.log('Log recorded successfully', response.data)
        }).catch(error => {
          console.error('Log recording failed', error)
        })
        this.$message({
          type: 'success',
          message: 'Data deleted successfully!'
        })
        this.$store.dispatch('gambling/gamblingRecreateTable').then(response => {
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: 'Operation cancelled.'
        })
      })
    },
    download() {
      logChange({
        change: 'GamblingTrans download',
        result: 'success'
      }).then(response => {
        console.log('Log recorded successfully', response.data)
      }).catch(error => {
        console.error('Log recording failed', error)
      })
      window.location.href = '/api_gambling/gambling/download/'
    },
    init() {
      this.$store.dispatch('gambling/userInitGambling', this.userAmount).then(() => {
        this.showUserAge()
        // this.showUserJob()

        this.$store.dispatch('gambling/storeInitGambling', this.storeAmount).then(() => {
          this.showChartStoreBig()

          this.$store.dispatch('gambling/cardInitGambling', '1').then(() => {
            this.showChartCard()
            this.$store.dispatch('gambling/consumeInitGambling').then(() => {
              this.showChartConsume()

              // this.$store.dispatch('gambling/transferInitGambling').then(() => {
              // this.showChartTrans()

              this.$store.dispatch('gambling/gamblingInit').then(response => {
                this.showChartGamble()
                this.showChartFraud()
              })
              // })
            })
          })
        })
      })
    },
    create() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          this.$confirm('Do you want to generate the data?', 'Tip', {
            confirmButtonText: 'Yes',
            cancelButtonText: 'No',
            type: 'warning'
          }).then(() => {
            logChange({
              change: 'GamblingTrans create',
              result: 'success'
            }).then(response => {
              console.log('Log recorded successfully', response.data)
            }).catch(error => {
              console.error('Log recording failed', error)
            })
            this.$message({
              type: 'success',
              message: 'Data generated successfully!'
            })
            const loadingInstanceUserAge = Loading.service({
              target: document.querySelector('#chartUserAge'),
              fullscreen: false
            })
            const loadingInstanceStoreBig = Loading.service({
              target: document.querySelector('#chartStoreBig'),
              fullscreen: false
            })
            const loadingInstanceCard = Loading.service({
              target: document.querySelector('#chartCard'),
              fullscreen: false
            })
            const loadingInstanceGambling = Loading.service({
              target: document.querySelector('#chartGambling'),
              fullscreen: false
            })
            const loadingInstanceFraud = Loading.service({
              target: document.querySelector('#chartFraud'),
              fullscreen: false
            })
            const loadingInstanceConsume = Loading.service({
              target: document.querySelector('#chartConsume'),
              fullscreen: false
            })
            // const loadingInstanceUserJob = Loading.service({
            //   target: document.querySelector('#chartUserJob'),
            //   fullscreen: false
            // })
            // const loadingInstanceTrans = Loading.service({
            //   target: document.querySelector('#chartTrans'),
            //   fullscreen: false
            // })

            this.$store.dispatch('gambling/durationChooseGambling',
              { startDate: this.form.startDate, duration: this.form.duration }).then(() => {
              console.log(this.form.startDate)
              this.$store.dispatch('gambling/userGenerateGambling', this.userAmount).then(() => {
                loadingInstanceUserAge.close()
                // loadingInstanceUserJob.close()
                this.showUserAge()
                // this.showUserJob()

                this.$store.dispatch('gambling/storeGenerateGambling', this.storeAmount).then(() => {
                  loadingInstanceStoreBig.close()
                  this.showChartStoreBig()

                  this.$store.dispatch('gambling/cardGenerateGambling', '1').then(() => {
                    loadingInstanceCard.close()
                    this.showChartCard()

                    this.dispatchCon().then(() => {
                      // loadingInstanceConsume.close()
                      // this.showChartConsume()
                      this.dispatchTran().then(() => {
                        // loadingInstanceTrans.close()
                        // this.showChartTrans()
                        loadingInstanceConsume.close()
                        this.showChartConsume()
                        this.$store.dispatch('gambling/gamblingGenerate', this.form).then(response => {
                          loadingInstanceGambling.close()
                          loadingInstanceFraud.close()
                          this.showChartGamble()
                          this.showChartFraud()
                        })
                      })
                    })
                  })
                })
              })
            })
          }).catch(() => {
            this.$message({
              type: 'info',
              message: 'Operation cancelled.'
            })
          })
        } else {
          return false
        }
      })
    },
    showUserAge() {
      this.chart = echarts.init(document.getElementById('chartUserAge'))
      var optionUserAge = {
        backgroundColor: 'rgba(128, 128, 128, 0.1)',
        title: {
          text: 'User age distribution',
          left: 'center'
          // padding: 40
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        dataZoom: [
          {
            height: 15,
            show: false,
            realtime: true,
            start: 35,
            end: 65
          },
          {
            type: 'inside',
            realtime: true,
            start: 35,
            end: 65
          }
        ],
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            name: 'Age',
            // data: ['0-18', '18-30', '30-39', '40-49', '50-59', '60-65', '>=66'],
            data: this.gambling_user_data['user_age_data_1'],
            axisTick: {
              alignWithLabel: true
            }
          }
        ],
        yAxis: [
          {
            type: 'value',
            name: 'People',
            nameGap: '15'
          }
        ],
        color: ['#00437C'],
        series: [
          {
            name: 'People',
            type: 'bar',
            barWidth: '60%',
            // data: [10, 52, 200, 334, 390, 330, 220]
            data: this.gambling_user_data['user_age_data_2']
          }
        ]
      }
      this.chart.setOption(optionUserAge)
    },
    showChartStoreBig() {
      var pdTmp = []
      var pvTmp = []
      this.gambling_store_data['data_1'].forEach(item => {
        var pd = item[0]
        var pv = item[1]
        pdTmp.push(pd)
        pvTmp.push(pv)
      })
      if (pdTmp.length > 0 || pvTmp.length > 0) {
        this.store.parantClassdata = pdTmp
        this.store.parantClassvalue = pvTmp
        this.store.parantClassdata.forEach(item => {
          this.store.totaldata.push(item)
        })
        this.store.parantClassvalue.forEach(item => {
          this.store.totalvalue.push(item)
        })
        this.store.parantClassdata.forEach((item, i) => {
          this.store.dictClass.push({
            value: this.store.parantClassvalue[i],
            name: item
          })
        })
      }
      var cdTmp = []
      var cvTmp = []
      this.gambling_store_data['data_2'].forEach(item => {
        var cd = item[0]
        var cv = item[1]
        cdTmp.push(cd)
        cvTmp.push(cv)
      })
      if (cdTmp.length > 0 || cvTmp.length > 0) {
        this.store.childClassdata = cdTmp
        this.store.childClassvalue = cvTmp
        this.store.childClassdata.forEach(item => { //
          this.store.totaldata.push(item)
        })
        this.store.childClassvalue.forEach(item => { //
          this.store.totalvalue.push(item)
        })
      }
      this.chart = echarts.init(document.getElementById('chartStoreBig'))
      const colors = ['#007D85', '#00437C']
      var optionStoreBig = {
        title: {
          text: 'Distribution of merchant scale',
          left: 'center',
          padding: 10
        },
        backgroundColor: 'rgba(128, 128, 128, 0.1)',
        color: colors,
        tooltip: {
          trigger: 'none',
          axisPointer: {
            type: 'cross'
          }
        },
        legend: {
          top: '8%'
        },
        grid: {
          top: 90,
          bottom: 50
        },
        dataZoom: [{
          show: false,
          height: 5,
          xAxisIndex: [
            0
          ],
          bottom: 30,
          start: 10,
          end: 80,
          handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
          handleSize: '110%',
          handleStyle: {
            color: '#d3dee5'

          },
          textStyle: {
            color: '#fff'
          },
          borderColor: '#90979c'
        },
        {
          type: 'inside',
          show: true,
          height: 5,
          start: 1,
          end: 35
        }],
        xAxis: [
          {
            type: 'category',
            axisTick: {
              alignWithLabel: true
            },
            axisLine: {
              onZero: false,
              lineStyle: {
                color: colors[1]
              }
            },
            axisPointer: {
              label: {
                formatter: function(params) {
                  return (
                    'Number of industry categories  ' +
                      params.value +
                      (params.seriesData.length ? '：' + params.seriesData[0].data : '')
                  )
                }
              }
            },
            data: this.store.parantClassdata
          },
          {
            type: 'category',
            axisTick: {
              alignWithLabel: true
            },
            axisLine: {
              onZero: false,
              lineStyle: {
                color: colors[0]
              }
            },
            axisPointer: {
              label: {
                formatter: function(params) {
                  return (
                    'Number of industry subcategories  ' +
                      params.value +
                      (params.seriesData.length ? '：' + params.seriesData[0].data : '')
                  )
                }
              }
            },
            data: this.store.childClassdata
          }
        ],
        yAxis: [
          {
            type: 'value',
            name: 'Amount (units)',
            nameGap: '30'
          }
        ],
        series: [
          {
            name: 'Industry subcategory',
            type: 'line',
            xAxisIndex: 1,
            smooth: true,
            emphasis: {
              focus: 'series'
            },
            data: this.store.childClassvalue
          },
          {
            name: 'Industry category',
            type: 'line',
            smooth: true,
            emphasis: {
              focus: 'series'
            },
            data: this.store.parantClassvalue
          }
        ]
      }
      this.chart.setOption(optionStoreBig)
    },
    showChartCard() {
      var cardsOwnerTypeTmp = []
      this.gambling_card_data.forEach(item => {
        var objTmp = {
          value: item.value,
          name: item.name
        }
        cardsOwnerTypeTmp.push(objTmp)
      })
      if (cardsOwnerTypeTmp.length > 0) {
        this.cardsOwnerType = cardsOwnerTypeTmp
      }
      this.chart = echarts.init(document.getElementById('chartCard'))
      var optionCard = {
        backgroundColor: 'rgba(128, 128, 128, 0.1)',
        title: {
          text: 'Bank card size distribution',
          left: 'center'
          // top: '5%',
          // textStyle: {
          //   fontSize: 30
          // }
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'horizontal',
          bottom: 'bottom',
          itemWidth: 15,
          itemHeight: 15,
          itemGap: 10
        },
        color: ['#00437C', '#007D85'],
        series: [
          {
            name: 'Number of bank cards',
            type: 'pie',
            radius: '60%',
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            },
            data: this.cardsOwnerType
          }
        ]
      }
      this.chart.setOption(optionCard)
    },
    showChartGamble() {
      this.chart = echarts.init(document.getElementById('chartGambling'))
      var optionGamble = {
        backgroundColor: 'rgba(128, 128, 128, 0.1)',
        title: {
          text: 'Transaction size distribution',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },

        legend: {
          orient: 'horizontal',
          bottom: 'bottom',
          itemWidth: 20,
          itemHeight: 20,
          itemGap: 10
        },
        color: ['#007D85', '#FC001B'],
        series: [
          {
            name: 'Number',
            type: 'pie',
            radius: ['30%', '60%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '25',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: this.gambling_data['data_1']
          }
        ]
      }
      this.chart.setOption(optionGamble)
    },
    showChartConsume() {
      this.chart = echarts.init(document.getElementById('chartConsume'))
      var optionConsume = {
        backgroundColor: 'rgba(128, 128, 128, 0.1)',
        title: {
          text: 'Normal transaction',
          left: 'center'
        },
        tooltip: {
          trigger: 'axis'
        },
        grid: {
          left: '4%',
          right: '5%',
          bottom: '3%',
          containLabel: true
        },
        dataZoom: [{
          show: false,
          height: 5,
          xAxisIndex: [
            0
          ],
          bottom: 30,
          start: 10,
          end: 80,
          handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
          handleSize: '110%',
          handleStyle: {
            color: '#d3dee5'

          },
          textStyle: {
            color: '#fff'
          },
          borderColor: '#90979c'
        },
        {
          type: 'inside',
          show: true,
          height: 5,
          start: 1,
          end: 35
        }],
        xAxis: {
          name: 'Time',
          type: 'category',
          boundaryGap: false,
          axisLabel: {
            rotate: 45
          },
          data: this.gambling_consume_data['trans_time']
          // data: ['20151212', '20161212', '20181212', '20191212', '20201212', '20211212', '20221212']
        },
        yAxis: {
          type: 'value',
          name: 'Amount (CNY)'
        },
        color: ['#007D85'],
        series: [
          {
            name: 'Amount (CNY)',
            type: 'line',
            stack: 'Total',
            data: this.gambling_consume_data['trans_amount']
            // data: [120, 132, 101, 134, 90, 230, 210]
          }
        ]
      }
      this.chart.setOption(optionConsume)
    },
    showChartFraud() {
      this.chart = echarts.init(document.getElementById('chartFraud'))
      var optionFraud = {
        backgroundColor: 'rgba(128, 128, 128, 0.1)',
        title: {
          text: 'Abnormal transaction',
          left: 'center'
        },
        tooltip: {
          trigger: 'axis'
        },
        grid: {
          left: '4%',
          right: '5%',
          bottom: '3%',
          containLabel: true
        },
        dataZoom: [{
          show: false,
          height: 5,
          xAxisIndex: [
            0
          ],
          bottom: 30,
          start: 10,
          end: 80,
          handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
          handleSize: '110%',
          handleStyle: {
            color: '#d3dee5'

          },
          textStyle: {
            color: '#fff'
          },
          borderColor: '#90979c'
        },
        {
          type: 'inside',
          show: true,
          height: 5,
          start: 1,
          end: 35
        }],
        xAxis: {
          name: 'Time',
          type: 'category',
          boundaryGap: false,
          axisLabel: {
            rotate: 45
          },
          // data: ['20151212', '20161212', '20181212', '20191212', '20201212', '20211212', '20221212']
          data: this.gambling_data['data_2']['trans_time']
        },
        yAxis: {
          type: 'value',
          name: 'Amount (CNY)'
        },
        color: ['#FC001B'],
        series: [
          {
            name: 'Amount (CNY)',
            type: 'line',
            stack: 'Total',
            // data: [120, 132, 101, 134, 90, 230, 210]
            data: this.gambling_data['data_2']['trans_amount']
          }
        ]
      }
      this.chart.setOption(optionFraud)
    }

    // showUserJob() {
    //   this.chart = echarts.init(document.getElementById('chartUserJob'))
    //   var optionUserJob = {
    //     backgroundColor: 'rgba(128, 128, 128, 0.1)',
    //     title: {
    //       text: 'Occupation distribution',
    //       left: 'center'

    //     },
    //     tooltip: {
    //       trigger: 'item',
    //       formatter: '{a} <br/>{b} : {c} ({d}%)'
    //     },
    //     color: ['#00437C', '#007D85', '#FC001B'],
    //     series: [
    //       {
    //         name: 'Number of users',
    //         type: 'pie',
    //         radius: [50, 200],
    //         // radius: ['30%', '60%'],
    //         center: ['50%', '60%'],
    //         roseType: 'area',
    //         itemStyle: {
    //           borderRadius: 8
    //         },
    //         label: {
    //           normal: {
    //             show: false
    //           }
    //         },
    //         // data: this.user.jobResult
    //         // data: this.register_user_data['user_job_data']
    //         data: this.gambling_user_data['user_job_data']
    //       }
    //     ]
    //   }
    //   this.chart.setOption(optionUserJob)
    // },
    // showChartTrans() {
    //   this.chart = echarts.init(document.getElementById('chartTrans'))
    //   var optionTrans = {
    //     backgroundColor: 'rgba(128, 128, 128, 0.1)',
    //     title: {
    //       text: 'Normal transfer',
    //       left: 'center'
    //     },
    //     tooltip: {
    //       trigger: 'axis'
    //     },
    //     grid: {
    //       left: '3%',
    //       right: '4%',
    //       bottom: '3%',
    //       containLabel: true
    //     },
    //     dataZoom: [{
    //       show: false,
    //       height: 5,
    //       xAxisIndex: [
    //         0
    //       ],
    //       bottom: 30,
    //       start: 10,
    //       end: 80,
    //       handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
    //       handleSize: '110%',
    //       handleStyle: {
    //         color: '#d3dee5'

    //       },
    //       textStyle: {
    //         color: '#fff'
    //       },
    //       borderColor: '#90979c'
    //     },
    //     {
    //       type: 'inside',
    //       show: true,
    //       height: 5,
    //       start: 1,
    //       end: 35
    //     }],
    //     xAxis: {
    //       name: 'Time',
    //       type: 'category',
    //       boundaryGap: false,
    //       axisLabel: {
    //         rotate: 45
    //       },
    //       data: this.gambling_transfer_data['trans_time']
    //       // data: ['20151212', '20161212', '20181212', '20191212', '20201212', '20211212', '20221212']
    //     },
    //     yAxis: {
    //       type: 'value',
    //       name: 'Amount (CNY)'
    //     },
    //     color: ['#00437C'],
    //     series: [
    //       {
    //         name: 'Amount (CNY)',
    //         type: 'line',
    //         stack: 'Total',
    //         data: this.gambling_transfer_data['trans_amount']
    //         // data: [120, 132, 101, 134, 90, 230, 210]
    //       }
    //     ]
    //   }
    //   this.chart.setOption(optionTrans)
    // },

  }

}

</script>

<style scoped>
  .chart-container{
    /* width: 50%; */
    float: left;
    overflow: hidden
  }
  .checkbox{
    position: absolute;
    margin-left: 170px;
    margin-top: 20px;
  }
  .gamb-header{
    margin: 10px auto;
    width: 100%;
    height: 345px;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5), 0 0 6px rgba(0, 0, 0, .04);
  }
  .el-input-number{
    width: 190px;
  }
  .shortLong{
    padding-top: 35px;
  }
  .checkData{
    position: absolute;
    /* margin-top: 12px; */
    margin-left: 53px;
  }
 /* .checkData label{
    margin-right: 71px;
  } */
  .durationDate{
    position: absolute;
    margin-top: 30px;
    margin-left: 570px;
  }
  .gambleGebtn{
    position: absolute;
   margin-left: 400px;
  }
</style>
