<template>
  <div class="app-container">
    <div class="market-header">
      <el-form id="marketingAllForm" ref="form" :model="form" :rules="rules" :inline="true" label-width="200px">
        <div class="shortLong">
          <el-form-item id="userAmount" label="Users count">
            <el-input-number
              v-model="userAmount"
              controls-position="right"
              :min="20"
            />
          </el-form-item>
          <el-form-item label="Bonus users count">
            <el-input-number v-model="form.user" :min="1" label="Description text" />
          </el-form-item>
          <el-form-item label="Clothing industry ratio">  <!--cloth_ratio-->
            <el-input-number v-model="form.clothRatio" :precision="2" :step="0.01" :min="0.01" :max="1.00" controls-position="right" />
          </el-form-item>
        </div>
        <el-form-item id="storeAmount" label="Merchants count">
          <el-input-number
            v-model="storeAmount"
            controls-position="right"
            :min="10"
          />
        </el-form-item>
        <el-form-item label="Frauded merchants count" class="marketFraud">
          <el-input-number v-model="form.store" :min="1" label="Description text" />
        </el-form-item>
        <el-form-item label="Life service ratio">  <!--life_service_ratio-->
          <el-input-number v-model="form.serviceRatio" :precision="2" :step="0.01" :min="0.01" :max="1.00" controls-position="right" />
        </el-form-item>

        <!-- <div class="durationDate"> -->
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
            type="date"
            placeholder="Select start date"
            format="yyyy-MM-dd"
            value-format="yyyyMMdd"
            :picker-options="pickerOptions"
            :disabled="btnDisabled"
          />
        </el-form-item>
        <el-form-item label="Operating hours ratio">  <!--is_in_opening_time-->
          <el-input-number v-model="form.openTime" :precision="2" :step="0.01" :min="0.01" :max="1.00" controls-position="right" />
        </el-form-item>
        <!-- </div> -->

        <el-checkbox-group v-model="checkList" class="checkData">
          <el-checkbox label="Normal transaction data generation" border size="big" @change="conC" />
        </el-checkbox-group>
        <div class="marketGebtn">
          <el-button type="primary" round size="large" @click="create()">Data generation</el-button>
          <el-button type="default" round size="large" @click="reset()">Parameter reset</el-button>
          <el-button type="default" round size="large" @click="download()">Data download</el-button>
          <el-button type="danger" round size="large" @click="deleteData()">Data deletion</el-button>
        </div>

      </el-form>
    </div>
    <div class="chart-container" style="width: 25%;">
      <div id="chartCard" class="chart" style="height:200px;width:100%;padding: 5px;" />
      <div id="chartMarketing" class="chart" style="height:200px;width:100%;padding: 5px;" />
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
      storeAmount: 10,
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
        startDate: '20221001',
        store: 5,
        user: 5,
        duration: 30,
        openTime: 1,
        clothRatio: 0.45,
        serviceRatio: 0.45
      }
    }
  },
  computed: {
    ...mapGetters([
      'marketing_user_data',
      'marketing_store_data',
      'marketing_card_data',
      'marketing_consume_data',
      'marketing_transfer_data',
      'marketing_date_data',
      'marketing_data'
    ])
  },
  beforeCreate() {
    this.$store.dispatch('marketing/durationSetMarketing').then(() => {
      this.form.startDate = this.$store.state.marketing.marketing_date_data.startDate
      this.form.duration = this.$store.state.marketing.marketing_date_data.duration
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
        return this.$store.dispatch('marketing/consumeGenerateMarketing', { date: this.form.startDate, duration: this.form.duration })
      } else {
        console.log('consumeInit')
        return this.$store.dispatch('marketing/consumeInitMarketing', { date: this.form.startDate, duration: this.form.duration })
      }
    },
    dispatchTran() {
      if (this.is_tran) {
        console.log('transferGenerate')
        return this.$store.dispatch('marketing/transferGenerateMarketing', { date: this.form.startDate, duration: this.form.duration })
      } else {
        console.log('transferInit')
        return this.$store.dispatch('marketing/transferInitMarketing', { date: this.form.startDate, duration: this.form.duration })
      }
    },
    reset() {
      this.userAmount = 50
      this.storeAmount = 10
      this.is_con = false
      this.is_tran = false
      this.checkList.pop()
      this.checkList.pop()
      this.form.startDate = '20221001'
      this.form.duration = 30
      this.form.store = 5
      this.form.user = 5
      this.form.openTime = 1
      this.form.clothRatio = 0.45
      this.form.serviceRatio = 0.45
      logChange({
        change: 'MarketingFraud reset',
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
          change: 'MarketingFraud deleteData',
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
        this.$store.dispatch('marketing/marketingRecreateTable').then(response => {
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
        change: 'MarketingFraud download',
        result: 'success'
      }).then(response => {
        console.log('Log recorded successfully', response.data)
      }).catch(error => {
        console.error('Log recording failed', error)
      })
      window.location.href = '/api_marketing/marketing/download/'
    },
    init() {
      this.$store.dispatch('marketing/userInitMarketing', this.userAmount).then(() => {
        this.showUserAge()
        // this.showUserJob()

        this.$store.dispatch('marketing/storeInitMarketing', this.storeAmount).then(() => {
          this.showChartStoreBig()

          this.$store.dispatch('marketing/cardInitMarketing', '1').then(() => {
            this.showChartCard()
            this.$store.dispatch('marketing/consumeInitMarketing').then(() => {
              this.showChartConsume()

              // this.$store.dispatch('marketing/transferInitMarketing').then(() => {
              // this.showChartTrans()

              this.$store.dispatch('marketing/marketingInit').then(response => {
                this.showChartMarket()
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
              change: 'MarketingFraud create',
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
            const loadingInstanceMarketing = Loading.service({
              target: document.querySelector('#chartMarketing'),
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

            this.$store.dispatch('marketing/durationChooseMarketing',
              { startDate: this.form.startDate, duration: this.form.duration }).then(() => {
              console.log(this.form.startDate)

              this.$store.dispatch('marketing/userGenerateMarketing', this.userAmount).then(() => {
                loadingInstanceUserAge.close()
                // loadingInstanceUserJob.close()
                this.showUserAge()
                // this.showUserJob()

                this.$store.dispatch('marketing/storeGenerateMarketing', this.storeAmount).then(() => {
                  loadingInstanceStoreBig.close()
                  this.showChartStoreBig()

                  this.$store.dispatch('marketing/cardGenerateMarketing', '1').then(() => {
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
                        this.$store.dispatch('marketing/marketingGenerate', this.form).then(response => {
                          loadingInstanceMarketing.close()
                          loadingInstanceFraud.close()
                          this.showChartMarket()
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
            data: this.marketing_user_data['user_age_data_1'],
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
            data: this.marketing_user_data['user_age_data_2']
          }
        ]
      }
      this.chart.setOption(optionUserAge)
    },
    showChartStoreBig() {
      var pdTmp = []
      var pvTmp = []
      this.marketing_store_data['data_1'].forEach(item => {
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
      this.marketing_store_data['data_2'].forEach(item => {
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
      this.marketing_card_data.forEach(item => {
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
    showChartMarket() {
      this.chart = echarts.init(document.getElementById('chartMarketing'))
      var optionMarket = {
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
            data: this.marketing_data['data_1']
          }
        ]
      }
      this.chart.setOption(optionMarket)
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
          // data: ['20151212', '20161212', '20181212', '20191212', '20201212', '20211212', '20221212']
          data: this.marketing_consume_data['trans_time']
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
            // data: [120, 132, 101, 134, 90, 230, 210]
            data: this.marketing_consume_data['trans_amount']
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
          data: this.marketing_data['data_2']['trans_time']
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
            data: this.marketing_data['data_2']['trans_amount']
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
    //         center: ['50%', '50%'],
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
    //         data: this.marketing_user_data['user_job_data']
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
    //       data: this.marketing_transfer_data['trans_time']
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
    //         // data: [120, 132, 101, 134, 90, 230, 210]
    //         data: this.marketing_transfer_data['trans_amount']
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
  .market-header{
    margin: 10px auto;
    width: 100%;
    height: 285px;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5), 0 0 6px rgba(0, 0, 0, .04);
  }
  .el-input-number{
    width: 220px;
  }
  .shortLong{
    padding-top: 35px;
  }
  .durationDate{
    position: absolute;
    margin-top: 30px;
    margin-left: 570px;
  }
  .checkData{
    position: absolute;
    /* margin-top: 12px; */
    margin-left: 60px;
  }
 /* .checkData label{
    margin-right: 71px;
  } */
  .marketGebtn{
    position: absolute;
    margin-left: 390px;
  }

</style>
