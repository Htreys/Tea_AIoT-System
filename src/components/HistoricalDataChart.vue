<template>
  <div>
    <canvas id="myChart"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';
import * as XLSX from 'xlsx';

Chart.register(...registerables);

export default {
  name: 'HistoricalDataChart',
  mounted() {
    this.loadExcelData();
  },
  methods: {
    loadExcelData() {
      // 使用 XLSX 读取本地 Excel 文件
      fetch('./data.xlsx')
          .then((res) => res.arrayBuffer())
          .then((buffer) => {
            const workbook = XLSX.read(buffer, { type: 'buffer' });
            const worksheetName = workbook.SheetNames[0];
            const worksheet = workbook.Sheets[worksheetName];
            const jsonData = XLSX.utils.sheet_to_json(worksheet);
            this.initializeChart(jsonData);
          });
    },
    initializeChart(data) {
      // 初始化图表数据
      const labels = data.map((d) => d.Disease);
      const counts = data.map((d) => d.Count);

      const ctx = document.getElementById('myChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: '次数',
            data: counts,
            backgroundColor: [
              'rgba(255, 159, 64, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(255, 99, 132, 0.2)',
              'rgba(199, 199, 199, 0.2)'
            ],
            borderColor: [
              'rgba(255, 159, 64, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 99, 132, 1)',
              'rgba(199, 199, 199, 1)'
            ],
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          },
          indexAxis: 'y', // 使图表变为水平条形图
        }
      });
    }
  }
};
</script>

<style scoped>
#myChart {
  max-width: 800px; /* 或者您希望的任何宽度 */
  max-height: 800px;
  margin: auto;
  display: block;
}
</style>
