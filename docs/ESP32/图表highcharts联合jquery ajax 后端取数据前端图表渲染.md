# 图表highcharts联合jquery ajax 后端取数据前端图表渲染

[![img](https://s3.51cto.com//wyfs02/M02/10/83/wKiom1LODQ-Rwd-oAAAs4WUVhV0798_middle.jpg)](http://blog.51cto.com/rfyiamcool)

rfyiamcool

关注

9人评论



13746人阅读

2013-06-13 13:44:30



Highcharts是一个制作图表的纯Javascript类库，主要特性如下：

- 兼容性：兼容当今所有的浏览器，包括iPhone、IE和火狐等等；
- 对个人用户完全免费；
- 纯JS，无BS；
- 支持大部分的图表类型：直线图，曲线图、区域图、区域曲线图、柱状图、饼装图、散布图；
- 跨语言：不管是PHP、Asp.net还是Java都可以使用，它只需要三个文件：一个是Highcharts的核心文件highcharts.js，还有a canvas emulator for IE和Jquery类库或者MooTools类库；
- 提示功能：鼠标移动到图表的某一点上有提示信息；
- 放大功能：选中图表部分放大，近距离观察图表；
- 易用性：无需要特殊的开发技能，只需要设置一下选项就可以制作适合自己的图表；
- 时间轴：可以精确到毫秒；



Highcharts提供大量的选项配置参数，您可以轻松定制符合用户要求的图表，目前官网只提供英文版的开发配置说明文档，而中文版的文档网上甚少，且零散不全。这里，我把Highcharts常用的最核心的参数选项配置整理成文档，与大家分享。

#### Chart：图表区选项

Chart图表区选项用于设置图表区相关属性。

| 参数                | 描述                                                         | 默认值  |
| ------------------- | ------------------------------------------------------------ | ------- |
| backgroundColor     | 设置图表区背景色                                             | #FFFFFF |
| borderWidth         | 设置图表边框宽度                                             | 0       |
| borderRadius        | 设置图表边框圆角角度                                         | 5       |
| renderTo            | 图表放置的容器，一般在html中放置一个DIV，获取DIV的id属性值   | null    |
| defaultSeriesType   | 默认图表类型line, spline, area, areaspline, column, bar, pie , scatter | 0       |
| width               | 图表宽度，默认根据图表容器自适应宽度                         | null    |
| height              | 图表高度，默认根据图表容器自适应高度                         | null    |
| margin              | 设置图表与其他元素之间的间距，数组，如[0,0,0,0]              | [null]  |
| plotBackgroundColor | 主图表区背景色，即X轴与Y轴围成的区域的背景色                 | null    |
| plotBorderColor     | 主图表区边框的颜色，即X轴与Y轴围成的区域的边框颜色           | null    |
| plotBorderWidth     | 主图表区边框的宽度                                           | 0       |
| shadow              | 是否设置阴影，需要设置背景色backgroundColor。                | false   |
| reflow              | 是否自使用图表区域高度和宽度，如果没有设置width和height时，会自适应大小。 | true    |
| zoomType            | 拖动鼠标进行缩放，沿x轴或y轴进行缩放，可以设置为：'x','y','xy' | ''      |
| events              | 事件回调，支持addSeries方法，click方法，load方法，selection方法等的回调函数。 |         |

#### Color：颜色选项

Color颜色选项用于设置图表的颜色方案。

| 参数  | 描述                                               | 默认值 |
| ----- | -------------------------------------------------- | ------ |
| color | 用于展示图表，折线/柱状/饼状等图的颜色，数组形式。 | array  |

Highcharts已经默认提供了多种颜色方案，当要显示的图形多于颜色种类时，多出的图形会自动从第一种颜色方案开始选取。自定义颜色方案的方法：

```
Highcharts.setOptions({
    colors: ['#058DC7', '#50B432', '#ED561B', '#DDDF00', '#24CBE5', '#64E572', '#FF9655', 
'#FFF263', '#6AF9C4'] 
}); 
```

#### Title：标题选项

Title标题选项用于设置图表的标题相关属性。

| 参数          | 描述                                                         | 默认值                               |
| ------------- | ------------------------------------------------------------ | ------------------------------------ |
| text          | 标题文本内容。                                               | Chart title                          |
| align         | 水平对齐方式。                                               | center                               |
| verticalAlign | 垂直对齐方式。                                               | top                                  |
| margin        | 标题与副标题之间或者主图表区间的间距。                       | 15                                   |
| floating      | 是否浮动，如果为true，则标题可以偏离主图表区，可配合x,y属性使用。 | false                                |
| style         | 设置CSS样式。                                                | {color: '#3E576F', fontSize: '16px'} |

#### Subtitle：副标题选项

副标题提供的属性选项与标题title大致相同，可参照上述标题选项，值得一提的是副标题的text选项默认为''，即空的，所以默认情况下副标题不显示。

#### xAxis：X轴选项

X轴选项用于设置图表X轴相关属性。

| 参数          | 描述                                                         | 默认值  |
| ------------- | ------------------------------------------------------------ | ------- |
| categories    | 设置X轴分类名称，数组，例如：categories: ['Apples', 'Bananas', 'Oranges'] | []      |
| title         | X轴名称，支持text、enabled、align、rotation、style等属性     |         |
| labels        | 设置X轴各分类名称的样式style，格式formatter，角度rotation等。 | array   |
| max           | X轴最大值(categories为空时)，如果为null，则最大值会根据X轴数据自动匹配一个最大值。 | null    |
| min           | X轴最小值(categories为空时)，如果为null，则最小值会根据X轴数据自动匹配一个最小值。 | array   |
| gridLineColor | 网格（竖线）颜色                                             | #C0C0C0 |
| gridLineWidth | 网格(竖线)宽度                                               | 1       |
| lineColor     | 基线颜色                                                     | #C0D0E0 |
| lineWidth     | 基线宽度                                                     | 0       |

#### yAxis：Y轴选项

Y轴选项与上述xAxis选项基本一致，请参照上表中的参数设置，不再单独列出。

#### Series：数据列选项

数据列选项用于设置图表中要展示的数据相关的属性。

| 参数 | 描述                                                         | 默认值 |
| ---- | ------------------------------------------------------------ | ------ |
| data | 显示在图表中的数据列，可以为数组或者JSON格式的数据。如：data:[0, 5, 3, 5]，或 data: [{name: 'Point 1',y: 0}, {name: 'Point 2',y: 5}] | ''     |
| name | 显示数据列的名称。                                           | ''     |
| type | 数据列类型，支持 area, areaspline, bar, column, line, pie, scatter or spline | line   |

#### plotOptions：数据点选项

plotOptions用于设置图表中的数据点相关属性。plotOptions根据各种图表类型，其属性设置略微有些差异，现将常用选项列出来。

| 参数             | 描述                         | 默认值                                 |
| ---------------- | ---------------------------- | -------------------------------------- |
| enabled          | 是否在数据点上直接显示数据   | false                                  |
| allowPointSelect | 是否允许使用鼠标选中数据点   | false                                  |
| formatter        | 回调函数，格式化数据显示内容 | formatter: function() {return this.y;} |

#### Tooltip：数据点提示框

Tooltip用于设置当鼠标滑向数据点时显示的提示框信息。

| 参数            | 描述                                                         | 默认值                   |
| --------------- | ------------------------------------------------------------ | ------------------------ |
| enabled         | 是否显示提示框                                               | true                     |
| backgroundColor | 设置提示框的背景色                                           | rgba(255, 255, 255, .85) |
| borderColor     | 提示框边框颜色，默认自动匹配数据列的颜色                     | auto                     |
| borderRadius    | 提示框圆角度                                                 | 5                        |
| shadow          | 是否显示提示框阴影                                           | true                     |
| style           | 设置提示框内容样式，如字体颜色等                             | color:'#333'             |
| formatter       | 回调函数，用于格式化输出提示框的显示内容。返回的内容支持html标签如：<b>, <strong>, <i>, <em>, <br/>, <span> | 2                        |

#### Legend：图例选项

legend用于设置图例相关属性。

| 参数            | 描述                                       | 默认值     |
| --------------- | ------------------------------------------ | ---------- |
| layout          | 显示形式，支持水平horizontal和垂直vertical | horizontal |
| align           | 对齐方式。                                 | center     |
| backgroundColor | 图例背景色。                               | null       |
| borderColor     | 图例边框颜色。                             | #909090    |
| borderRadius    | 图例边框角度                               | 5          |
| enabled         | 是否显示图例                               | true       |
| floating        | 是否可以浮动，配合x，y属性。               | false      |
| shadow          | 是否显示阴影                               | false      |
| style           | 设置图例内容样式                           | ''         |





第一个例子：



这个是从后端api取值，后端再从数据库里取值。

为了不让整个页面刷新，用了ajax做局部刷新



[![mysql-mon_004.png](http://blog.51cto.com/attachment/201306/133955415.png)](http://blog.51cto.com/attachment/201306/133955415.png)



[![mysql-mon_003.png](http://blog.51cto.com/attachment/201306/134739773.png)](http://blog.51cto.com/attachment/201306/134739773.png)



```as3
$(function () {
    $(document).ready(function () {
                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                               
        ////////
        // Mysql Questions
        ////////
        var mysqlQuestionsOptions = {
            chart: {
                renderTo: 'mysql-questions-container',
                type: 'spline'
            },
            title: {
                text: '',
                x: -20 //center
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: {
                title: {
                    text: 'per second'
                }, min: 0
            },
            series: [{
                name: 'Select'
            },{
                name: 'Insert'
            },{
                name: 'Replace'
            },{
                name: 'Update'
            },{
                name: 'Delete'
            }]
        };
                                                                                                                                                                                                                                                                                 
        $.ajax({
            url: 'stats/mysql/questions',
            dataType: "json",
            success: function (data) {
                //init series arays
                select_arr = [];
                insert_arr = [];
                replace_arr = [];
                update_arr = [];
                delete_arr =[];
                for (i in data) {
                    //build
                    var r = data[i];
                    select_arr.push([r.ts, r.Select_per_second]);
                    insert_arr.push([r.ts, r.Insert_per_second]);
                    replace_arr.push([r.ts, r.Replace_per_second]);
                    update_arr.push([r.ts, r.Update_per_second]);
                    delete_arr.push([r.ts, r.Delete_per_second]);
                }
                //save series
                mysqlQuestionsOptions.series[0].data = select_arr;
                mysqlQuestionsOptions.series[1].data = insert_arr;
                mysqlQuestionsOptions.series[2].data = replace_arr;
                mysqlQuestionsOptions.series[3].data = update_arr;
                mysqlQuestionsOptions.series[4].data = delete_arr;
                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                         
                var chart = new Highcharts.Chart(mysqlQuestionsOptions);
            },
            cache: false
        });
                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                 
        ////////
        // Mysql Select Sort
        ////////
        var mysqlSelectSortOptions = {
            chart: {
                renderTo: 'mysql-select-sort-container',
                type: 'spline'
            },
            title: {
                text: '',
                x: -20 //center
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: {
                title: {
                    text: 'per second'
                }, min: 0
            },
            series: [{
                name: 'Select Scan'
            },{
                name: 'Select Range'
            },{
                name: 'Select Full Join'
            },{
                name: 'Select Range Check'
            },{
                name: 'Select Full Range Join'
            },{
                name: 'Sort Scan'
            },{
                name: 'Sort Range'
            },{
                name: 'Sort Merge Passes'
            }]
        };
                                                                                                                                                                                                                                                                                 
        $.ajax({
            url: 'stats/mysql/select_sort',
            dataType: "json",
            success: function (data) {
                //init series arays
                select_scan_arr = [];
                select_range_arr = [];
                select_full_join_arr = [];
                select_range_check_arr = [];
                select_full_range_join_arr =[];
                sort_scan_arr =[];
                sort_range_arr =[];
                sort_merge_passes_arr =[];
                for (i in data) {
                    //build
                    var r = data[i];
                    select_scan_arr.push([r.ts, r.Select_scan_per_sec]);
                    select_range_arr.push([r.ts, r.Select_range_per_sec]);
                    select_full_join_arr.push([r.ts, r.Select_full_join_per_sec]);
                    select_range_check_arr.push([r.ts, r.Select_range_check_per_sec]);
                    select_full_range_join_arr.push([r.ts, r.Select_full_range_join_per_sec]);
                    sort_scan_arr.push([r.ts, r.Sort_scan_per_sec]);
                    sort_range_arr.push([r.ts, r.Sort_range_per_sec]);
                    sort_merge_passes_arr.push([r.ts, r.Sort_merge_passes_per_sec]);
                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                           
                }
                //save series
                mysqlSelectSortOptions.series[0].data = select_scan_arr;
                mysqlSelectSortOptions.series[1].data = select_range_arr;
                mysqlSelectSortOptions.series[2].data = select_full_join_arr;
                mysqlSelectSortOptions.series[3].data = select_range_check_arr;
                mysqlSelectSortOptions.series[4].data = select_full_range_join_arr;
                mysqlSelectSortOptions.series[5].data = sort_scan_arr;
                mysqlSelectSortOptions.series[6].data = sort_range_arr;
                mysqlSelectSortOptions.series[7].data = sort_merge_passes_arr;
                                                                                                                                                                                                                                                                                     
                var chart = new Highcharts.Chart(mysqlSelectSortOptions);
            },
            cache: false
        });
                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                 
        ////////
        // Mysql Connections
        ////////
        var mysqlConnectionsOptions = {
            chart: {
                renderTo: 'mysql-connections-container',
                type: 'spline'
            },
            title: {
                text: '',
                x: -20 //center
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: [{
                title: {
                    text: 'per second'
                }, min: 0
            },{
                title: {
                    text: 'count'
                }, min: 0,
                opposite: true
            }],
            series: [{
                name: 'Max Connections',
                yAxis : 1, type: 'area'
            },{
                name: 'Max Used Connections',
                yAxis : 1,  type: 'area'
            },{
                name: 'Process Count',
                yAxis : 1,  type: 'area'
            },{
                name: 'Running Process Count',
                yAxis : 1
            },{
                name: 'Connection Rate',
                yAxis : 0
            },{
                name: 'Aborted connects Rate',
                yAxis : 0
            },{
                name: 'Aborted clients Rate',
                yAxis : 0
            }]
        };
                                                                                                                                                                                                                                                                                 
        $.ajax({
            url: 'stats/mysql/connections',
            dataType: "json",
            success: function (data) {
                //init series arays
                connections_arr = [];
                aborted_connects_arr = [];
                aborted_clients_arr = [];
                max_used_connections_arr = [];
                max_connections_arr =[];
                process_count_arr = [];
                running_process_count_arr =[];
                for (i in data) {
                    //build
                    var r = data[i];
                    connections_arr.push([r.ts, r.Connections_per_second]);
                    aborted_connects_arr.push([r.ts, r.Aborted_connects_per_second]);
                    aborted_clients_arr.push([r.ts, r.Aborted_clients_per_second]);
                    max_used_connections_arr.push([r.ts, r.max_used_connections]);
                    max_connections_arr.push([r.ts, r.max_connections]);
                    process_count_arr.push([r.ts, r.process_count]);
                    running_process_count_arr.push([r.ts, r.process_count_non_sleep]);       
                }
                //save series
                mysqlConnectionsOptions.series[4].data = connections_arr;
                mysqlConnectionsOptions.series[5].data = aborted_connects_arr;
                mysqlConnectionsOptions.series[6].data = aborted_clients_arr;
                mysqlConnectionsOptions.series[0].data = max_connections_arr;
                mysqlConnectionsOptions.series[1].data = max_used_connections_arr;
                mysqlConnectionsOptions.series[2].data = process_count_arr;
                mysqlConnectionsOptions.series[3].data = running_process_count_arr;
                                                                                                                                                                                                                                                                                         
                var chart = new Highcharts.Chart(mysqlConnectionsOptions);
            },
            cache: false
        });
                                                                                                                                                                                                                                                                                 
        ////////
        // Mysql Bytes
        ////////
        var mysqlBytesOptions = {
            chart: {
                renderTo: 'mysql-bytes-container',
                type: 'spline'
            },
            title: {
                text: '',
                x: -20 //center
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: {
                title: {
                    text: 'kBps'
                }, min: 0
            },
            series: [{
                name: 'Sent'
            },{
                name: 'Recieved'
            }]
        };
                                                                                                                                                                                                                                                                                 
        $.ajax({
            url: 'stats/mysql/bytes',
            dataType: "json",
            success: function (data) {
                //init series arays
                sent = [];
                recieved =[];
                for (i in data) {
                    //build
                    var r = data[i];
                    sent.push([r.ts, r.kBps_sent]);
                    recieved.push([r.ts, r.kBps_recieved]);
                }
                //save series
                mysqlBytesOptions.series[0].data = sent;
                mysqlBytesOptions.series[1].data = recieved;
                var chart = new Highcharts.Chart(mysqlBytesOptions);
            },
            cache: false
        });
                                                                                                                                                                                                                                                                                 
        ////////
        // Mysql Temp
        ////////
        var mysqlTempOptions = {
            chart: {
                renderTo: 'mysql-temp-container',
                type: 'spline'
            },
            title: {
                text: '',
                x: -20 //center
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: {
                title: {
                    text: 'per minute'
                }, min: 0
            },
            series: [{
                name: 'Created Tmp Disk Tables'
            },{
                name: 'Created Tmp Tables'
            },{
                name: 'Created Tmp Files'
            }]
        };
                                                                                                                                                                                                                                                                                 
        $.ajax({
            url: 'stats/mysql/temp',
            dataType: "json",
            success: function (data) {
                //init series arays
                tmp_disk_tables = [];
                tmp_tables = [];
                tmp_files = [];
                for (i in data) {
                    //build
                    var r = data[i];
                    tmp_disk_tables.push([r.ts, r.Created_tmp_disk_tables_per_min]);
                    tmp_tables.push([r.ts, r.Created_tmp_tables_per_min]);
                    tmp_files.push([r.ts, r.Created_tmp_files_per_min]);
                                                                                                                                                                                                                                                                                         
                }
                //save series
                mysqlTempOptions.series[0].data = tmp_disk_tables;
                mysqlTempOptions.series[1].data = tmp_tables;
                mysqlTempOptions.series[2].data = tmp_files;
                var chart = new Highcharts.Chart(mysqlTempOptions);
            },
            cache: false
        });
                                                                                                                                                                                                                                                                                 
        ////////
        // Mysql Table Locks
        ////////
        var mysqlTableLocksOptions = {
            chart: {
                renderTo: 'mysql-table-locks-container',
                type: 'spline'
            },
            title: {
                text: '',
                x: -20 //center
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: {
                title: {
                    text: 'per second'
                }, min: 0
            },
            series: [{
                name: 'Table locks wait'
            },{
                name: 'Table locks immediate'
            }]
        };
                                                                                                                                                                                                                                                                                 
        $.ajax({
            url: 'stats/mysql/table_locks',
            dataType: "json",
            success: function (data) {
                //init series arays
                wait = [];
                immediate = [];
                for (i in data) {
                    //build
                    var r = data[i];
                    wait.push([r.ts, r.Table_locks_wait_per_sec]);
                    immediate.push([r.ts, r.Table_locks_immediate_per_sec]);
                }
                //save series
                mysqlTableLocksOptions.series[0].data = wait;
                mysqlTableLocksOptions.series[1].data = immediate;
                var chart = new Highcharts.Chart(mysqlTableLocksOptions);
            },
            cache: false
        });
                                                                                                                                                                                                                                                                                 
        ////////
        // Mysql Innodb Buffer Pool Usage
        ////////
        var mysqlInnoDBBPOptions = {
            chart: {
                renderTo: 'mysql-innodb-bp-container',
                type: 'area'
            },
            title: {
                text: 'Buffer Pool Usage',
                x: -20 //center
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: [{
                title: {
                    text: 'MBytes'
                }, min: 0
            },{
             title: {
                    text: 'Hit Rate %'
                }, min: 0,  max: 100, opposite: true
            }],
            series: [{
                name: 'Buffer Pool Total'
            },{
                name: 'Buffer Pool Used'
            },{
                name: 'Read Hit Rate', type: 'spline', yAxis: 1
            }]
        };
                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                 
        ////////
        // Mysql Innodb
        ////////
        var mysqlInnoDBOptions = {
            chart: {
                renderTo: 'mysql-innodb-container',
                type: 'spline'
            },
            title: {
                text: 'InnoDB Stats',
                x: -20 //center
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: {
                title: {
                    text: 'per second'
                }, min: 0
            },
            series: [{
                name: 'Buffer Pool Read Request'
            },{
                name: 'Buffer Pool Reads'
            },{
                name: 'Buffer Pool Read Ahead Rnd'
            },{
                name: 'Buffer Pool Read Ahead Seq'
            },{
                name: 'Buffer Pool Write Request'
            },{
                name: 'Buffer Pool Pages Flushed'
            },{
                name: 'Buffer Pool Wait Free'
            },{
                name: 'Row Lock Waits'
            },{
                name: 'Data Reads'
            },{
                name: 'Data Writes'
            },{
                name: 'Data Fsyncs'
            },{
                name: 'Pages Created'
            },{
                name: 'Pages Read'
            },{
                name: 'Pages Written'
            },{
                name: 'Rows Deleted'
            },{
                name: 'Rows Inserted'
            },{
                name: 'Rows Read'
            },{
                name: 'Rows Updated'
            }]
        };
                                                                                                                                                                                                                                                                                 
        $.ajax({
            url: 'stats/mysql/innodb',
            dataType: "json",
            success: function (data) {
                //init series arays
                bp_used = [];
                bp_total = [];
                bp_read_ratio = [];
                bp_read_requests = [];
                bp_reads = []
                bp_read_rnd = [];
                bp_read_seq = [];
                bp_write_req = [];
                bp_pages_flush = [];
                bp_wait_free = [];
                row_lock_waits = [];
                data_reads = [];
                data_write = [];
                data_fsyncs = [];
                pages_created = [];
                pages_read = [];
                pages_written = [];
                rows_deleted = [];
                rows_inserted = [];
                rows_read = [];
                rows_updated = [];
                for (i in data) {
                    //build
                    var r = data[i];
                    bp_used.push([r.ts, r.Innodb_buffer_pool_used_mb]);
                    bp_total.push([r.ts, r.Innodb_buffer_pool_total_mb]);
                    bp_read_ratio.push([r.ts, r.Innodb_buffer_pool_read_ratio]);
                    bp_read_requests.push([r.ts, r.Innodb_buffer_pool_read_requests_per_second]);
                    bp_reads.push([r.ts, r.Innodb_buffer_pool_reads_per_second]);
                    bp_read_rnd.push([r.ts, r.Innodb_buffer_pool_read_ahead_rnd_per_second]);
                    bp_read_seq.push([r.ts, r.Innodb_buffer_pool_read_ahead_seq_per_second]);
                    bp_write_req.push([r.ts, r.Innodb_buffer_pool_write_requests_per_second]);
                    bp_pages_flush.push([r.ts, r.Innodb_buffer_pool_pages_flushed_per_second]);
                    bp_wait_free.push([r.ts, r.Innodb_buffer_pool_wait_free_per_second]);
                    row_lock_waits.push([r.ts, r.Innodb_row_lock_waits_per_second]);
                    data_reads.push([r.ts, r.Innodb_data_reads_per_second]);
                    data_write.push([r.ts, r.Innodb_data_writes_per_second]);
                    data_fsyncs.push([r.ts, r.Innodb_data_fsyncs_per_second]);
                    pages_created.push([r.ts, r.Innodb_pages_created_per_second]);
                    pages_read.push([r.ts, r.Innodb_pages_read_per_second]);
                    pages_written.push([r.ts, r.Innodb_pages_written_per_second]);
                    rows_deleted.push([r.ts, r.Innodb_rows_deleted_per_second]);
                    rows_inserted.push([r.ts, r.Innodb_rows_inserted_per_second]);
                    rows_read.push([r.ts, r.Innodb_rows_read_per_second]);
                    rows_updated.push([r.ts, r.Innodb_rows_updated_per_second]);
                                                                                                                                                                                                                                                                                            
                }
                //save series
                mysqlInnoDBBPOptions.series[1].data = bp_used;
                mysqlInnoDBBPOptions.series[0].data = bp_total;
                mysqlInnoDBBPOptions.series[2].data =  bp_read_ratio;
                                                                                                                                                                                                                                                                                         
                mysqlInnoDBOptions.series[0].data = bp_read_requests;
                mysqlInnoDBOptions.series[1].data = bp_reads;
                mysqlInnoDBOptions.series[2].data = bp_read_rnd;
                mysqlInnoDBOptions.series[3].data = bp_read_seq;
                mysqlInnoDBOptions.series[4].data = bp_write_req;
                mysqlInnoDBOptions.series[5].data = bp_pages_flush;
                mysqlInnoDBOptions.series[6].data = bp_wait_free;
                mysqlInnoDBOptions.series[7].data = row_lock_waits;
                mysqlInnoDBOptions.series[8].data = data_reads;
                mysqlInnoDBOptions.series[9].data = data_write;
                mysqlInnoDBOptions.series[10].data = data_fsyncs;
                mysqlInnoDBOptions.series[11].data = pages_created;
                mysqlInnoDBOptions.series[12].data = pages_read;
                mysqlInnoDBOptions.series[13].data = pages_written;
                mysqlInnoDBOptions.series[14].data = rows_deleted;
                mysqlInnoDBOptions.series[15].data = rows_inserted;
                mysqlInnoDBOptions.series[16].data = rows_updated;
                                                                                                                                                                                                                                                                                         
                var chart = new Highcharts.Chart(mysqlInnoDBBPOptions);
                chart = new Highcharts.Chart(mysqlInnoDBOptions);
            },
            cache: false
        });
    });
});
$(document).scroll(function(){
    // If has not activated (has no attribute "data-top"
    if (!$('.subnav').attr('data-top')) {
        // If already fixed, then do nothing
        if ($('.subnav').hasClass('subnav-fixed')) return;
        // Remember top position
        var offset = $('.subnav').offset();
        $('.subnav').attr('data-top', offset.top);
    }
    if ($('.subnav').attr('data-top') - $('.subnav').outerHeight() <= $(this).scrollTop())
        $('.subnav').addClass('subnav-fixed');
    else
        $('.subnav').removeClass('subnav-fixed');
});
```







**第二个例子**



这个和前面是一样的方式，这里做了多个引用，也就是可以画多条线路

这个图不是我这的，但下面的代码是行的通的，可以放到一个js里面引用，然后通过ajax传值过去，在前端进行数据的渲染。



**![QQ%E6%88%AA%E5%9B%BE20120802234015.png](http://blog.51cto.com/attachment/201306/133858310.png)**







```as3
var charts = new Array();
        var serverCount = 6;
        var lastTimes = new Array();
        var max = ${params.int("max")?:120};
        $(document).ready(function() {
            Highcharts.setOptions({
                global: {
                    useUTC: false
                }
            });
            for (var i = 0; i < serverCount; i++) {
                charts[i] = new Highcharts.Chart({
                    chart: {
                        renderTo: 'container' + i,
                        type: 'spline',
                        events: {
                            load: function() {
                                // set up the updating of the chart each second
                                var series = this.series;
                                var serverIndex = i;
                                lastTimes[serverIndex] = 0;
                                var loadData = function() {
                                                                        $.getJSON("http://${request.serverName}:${request.serverPort}${request.contextPath}/toolkits/queryStatistics.gsp", {"lasTime":lastTimes[serverIndex],"proxy":true,"index":serverIndex,"max":max}, function(data) {
                                        for (var k = 0; k < series.length; k++) {
                                            for (var j = 0; j < data[k].length; j++) {
                                                var point = data[k][j];
                                                var isShift = series[k].data.length >= max;
                                                console.log("series " + k + ".data.length=" + series[k].data.length);
                                                var lastTime = 0;
                                                if (series[k].data.length > 0)
                                                    lastTime = series[k].data[series[k].data.length - 1].x;
                                                if (point[0] > lastTime)
                                                    series[k].addPoint([point[0],point[1]], true, isShift);
                                                lastTimes[serverIndex] = point[0];
                                            }
                                        }
                                    })
                                };
                                loadData();
                                setInterval(loadData, 60000);
                            }
                        }
                    },
                    title: {
                        text: '访问量实时监控'
                    },
                    xAxis: [
                        {
                            type: 'datetime',
                            tickPixelInterval: 120
                        }
                    ],
                    yAxis: [
                        {
                            title: {
                                text: '总请求/分钟',
                                style: {
                                    color: '#3E576F'
                                }
                            }
                        },
                        {
                            title: {
                                text: '平均响应时间',
                                style: {
                                    color: '#00AA00'
                                }
                            },opposite:true
                        }
                    ],
                    plotOptions: {
                        spline: {
                            marker:{
                                enabled: false,
                                states: {
                                    hover: {
                                        enabled: true,
                                        symbol: 'circle',
                                        radius: 5,
                                        lineWidth: 1
                                    }
                                }
                            }
                        }
                    },
                    tooltip: {
                        formatter: function() {
                            return '<b>' + this.series.name + '</b><br/>' +
                                    Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                                    Highcharts.numberFormat(this.y, 2);
                        }
                    },
                    legend: {
                        enabled: true
                    },
                    exporting: {
                        enabled: false
                    },
                    series: [
                        {
                            name: '总请求数',
                            data: []
                        },
                        {
                            name: '错误请求数',
                            data: []
                        },
                        {
                            name: '平均响应时间',
                            yAxis:1,
                            data: []
                        }
                    ]
                });
            }
        })
```



