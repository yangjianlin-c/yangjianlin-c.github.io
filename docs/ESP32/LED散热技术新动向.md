Date: 2014-09-15
Title: LED散热技术新动向
intro: 
Tags: LED,散热
Status: public

高功率LED发光效率进展飞速，相对也带来更严苛的散热挑战，由于从晶片、封装、基板至系统各层级环环相扣，因此须逐一克服难关才能真正符合市场的散热要求，其中FR4基板将為大势所趋；系统可透过关键元件改善散热难题，进而实现高可靠度、长寿命的LED灯具。

发光二极体(LED)具备轻薄、省电、环保、点亮反应快、长寿命等特点，加上在成本续降之下，光输出与功率仍不断提升，促使LED照明的市场接受度与日俱增，从交通号志指示灯至大尺寸背光源，进展到各种照明用途如车头灯、室内外照明灯具等。现阶段LED发光效率已突破每瓦100流明，足以取代耗电的白炽灯、卤素灯，甚至是萤光灯与高压气体放电灯。

伴随着高功率LED技术迭有进展，LED尺寸逐渐缩小，热量集中在小尺寸晶片内，且热密度更高，致使LED面临日益严苛的热管理考验。為降低LED热阻，其散热必须由晶片层级(Chip Level)、封装层级(Package Level)、散热基板层级(Board Level)到系统层级(System Level)，针对每一个环节进行最佳化的散热设计，以获得最佳的散热(图1)。

![](/uploadfiles/image/201304/8.jpg)

图1 LED散热策略

![](/uploadfiles/image/201304/9.jpg)

图2 高功率LED剖面图

从图2中，可以了解整个高功率LED元件温度定义，并利用公式1计算LED总热阻值。其中Rj-a為晶片与空气之间的热阻值(K/W)，此部分的热阻由晶片和封装造成，属于磊晶厂及封装厂商负责范畴。Rsp-h為散热基板与散热鰭片之间的热阻值(K/W)；Rh-a為散热鰭片与空气端的热阻值(K/W)，Rsp-h及Rh-a為灯具系统商所负责的区域，以下将针对各关键元件进行散热策略探讨。

![](/uploadfiles/image/201304/10.jpg)

## 藉尺寸/材料改善晶片散热

LED晶片发光同时亦会產生热能(光电转换效率约為25～35%)，造成晶片温度(Tj)提高，然LED所產生的热能是透过下方的传热底座传导(Tsp)，因此当LED点亮时，若无法快速与有效的将热量带走，将会造成亮度降低、寿命变短及波长飘移，甚至造成LED损坏，图3為科瑞(Cree)EZ1000的晶片示意图。

![](/uploadfiles/image/201304/11.jpg)

资料来源：Cree

图3 Cree-EZ1000的晶片示意图

晶片的散热策略可大致归纳為增加晶片尺寸和改变材料结构两种，晶片的热阻计算為Rchip=Lchip/(Kchip×Achip)，其中Lchip為热传路径的长度(蓝宝石基板厚度為100微米)；Kchip為总热导係数(蓝宝石约為35～40W/mK)；Achip為热传路径的截面积(40mil=1mm2)。根据上式，若将蓝宝石基板厚度由100微米缩短至80微米，晶片热阻可降低20%，但不能无限制的缩短造成晶圆片破片。另外，若将Kchip值提高至280W/mK(SiC)，晶片热阻可降低87.5%。因此，透过改变材料结构是目前较有效降低晶片热阻的方式。

## FR4散热基板成主流

![](/uploadfiles/image/201304/12.jpg)

一般对于常见LED的散热基板，大致可区分為传统印刷电路板环氧玻璃纤维板(FR4)、金属基印刷电路板(MCPCB)、陶瓷基板(AL2O3)及复合基板四种(表1)。 由于传统FR4的铜箔层散热能力有限，必须藉由较厚的金属层降低扩散热阻(Spreading Resistance)。另外再藉由介电层(Dielectrics)设计提高轴向上的热传速率，将热能迅速传导至散热鰭片。从价格和量產观点来看，印刷电路板优于其他基板，但其热传导係数低(热阻值高)，不利于LED散热，针对此缺点可透过以下几种方式进行改善：

### 合併导热孔降低热阻值

在LED的传热底座及周边范围，加上导热孔，并在其周围镀上一层铜箔层(35微米)，利用铜的高导热性，将传热底座的热能快速传递至下方的散热鰭片，以降低FR4散热基板热阻值达7K/W(图4)。

![](/uploadfiles/image/201304/13.jpg)

资料来源：Philips Lumileds

图4 FR4合併导热孔

### 合併导热孔/导热材料有助于缩减成本

利用类似第一种的製作程序，只是导热孔内加入高导热係数的材料，并在导热孔的上、下面与其周围镀上一层铜箔层(35微米)，藉由孔内的导热材料与孔周围的铜箔层，将传热底座的热能快速传递至下方的散热鰭片，降低FR4散热基板热阻值至3K/W(图5)。散热基板实体图如图6所示。

![](/uploadfiles/image/201304/14.jpg)

资料来源：Philips Lumileds

图5 FR4合併导热孔及导热材料

![](/uploadfiles/image/201304/15.jpg)

图6 FR4散热基板实体图

MCPCB是最常见的高功率LED散热基板，但此种基板最关键材料在于中间的介电绝缘层(Epoxy)，若是使用较高导热係数的绝缘层材料，才能使LED的热能快速透过下层的金属板扩散并传递至散热鰭片；反之，使用低导热材料，则热能无法有效传递至金属基板，形成高热阻抗，其传热性能差异如图7所示。 从图8热阻比较图中可知，若是採用FR4合併导热孔和导热材料製程，可将散热基板热阻值减少，并降低散热基板成本。

![](/uploadfiles/image/201304/16.jpg)

图7 不同导热材料形成的热阻值比较

![](/uploadfiles/image/201304/17.jpg)

资料来源：Philips Lumileds

图8 不同散热基板热阻值比较图

### 透过散热元件提高系统散热效能

对于系统端的散热策略，常见的散热元件為鰭片(Heat Sink)、热管(Heat Pipes)、均温板(Vapor Chamber)、迴路式热管(Loop Heat Pipe, LHP)及压电风扇(Piezo Fans)。以下為各元件原理介绍及优缺点。

### 散热鰭片应用最為普及

散热鰭片主要是靠传导与自然对流方式进行散热，為最常见的散热方式，利用增加散热面积与搭配风道、开气孔设计，提升传导和自然对流能力，缺点為重量和落尘堆积造会成散热不良。常见的散热鰭片种类如图9所示。

![](/uploadfiles/image/201304/18.jpg)

图9 散热鰭片实体图

### 热管可达成迅速散热

热管在电脑的应用相当广泛，近年来亦被应用在LED灯具，不外乎是看重其质量轻且结构简单、传热迅速且无动件及毋须外加电源优点。因此，针对LED热密度极高的状况下，热管可快速散热。然其缺点有温度范围限制、传热路径较短及受重力影响时具方向性，因此应用在LED灯具无法将热源有效带至远处，即便热管能将热源迅速带离开，但仍须搭配各种散热鰭片增加与空气的接触面积，进而增加自然对流的能力(图10)。

![](/uploadfiles/image/201304/20.jpg)

图10 热管实体图

均温板局限灯具外观设计

均温板、热管原理与理论架构相同，只有热传导的方向不同，热管的热传导方式是一维的，是线的热传导方式；而均温板的热传导方式係二维，是面的热传导方式，因此均温板可将热源均匀扩散开来，以降低扩散热阻。但即便均温板在灯具应用仅能為垂直方向传递，不如热管可把热往水平或垂直方向传递，所以在灯具外型设计受限较大(图11)。

![](/uploadfiles/image/201304/19.jpg)

图11 均温板实体图

迴路式热管实现长距离热传导

迴路式热管是依靠封闭式迴路管内的工质，在加热端与冷却端的热交换进而达成热量传递。热量从加热端传递给工质，使工质变成蒸气。而当蒸气流经冷却端时，其被冷凝成液体，而加热端内部的毛细结构可利用毛细力将冷凝液体带回蒸发器，如此即可完成流体循环，达成热能的传递。除一般传统热管的优点外，迴路式热管最吸引人之处在于它可做长距离热量传递、管路可弯曲，因此极富灵活性且不受重力场的影响，任何方向均可操作。因此藉由迴路式热管远距离热传特性，将LED热源所释放出来的热藉由铜管迴路传递至灯壳上(散热板)，并利用大面积灯壳表面与空气接触，在自然对流运\\\\作下，毋须借助任何额外电力，可不断循环散热，有效解决散热的问题，进而提升LED灯具寿命(图12)。

![](/uploadfiles/image/201304/21.jpg)

图12 应用LHP的LED灯具实体图

压电风扇适合室内灯具应用

相较于一般的传统风扇而言，压电风扇具备体积小、消耗功率小、噪音小、长寿命等优点，这些优点相当适用于现在室内LED灯具散热所需的低功率、低噪音和不占空间的要求。而压电风扇则是利用压电材料具有压电效应的特性来造成叶片的摆动，造成空气流动来带走LED產生的温度。一般选用压电风扇性能参数在于其压电参数、扇叶厚度和黏合胶(Bonding Glue)之不同。图13显示一个实际应用范例，此為一个室内灯具模组，搭配压电风扇及小面积散热鰭片，形成气流，提高对流热传係数。

![](/uploadfiles/image/201304/22.jpg)

资料来源：飞利浦

图13 主动式压电风扇散热

LED以其节能及环保特点有着广阔的应用空间，在照明领域中，LED发光產品的应用正吸引世人目光，一般来说，LED灯具能否稳定工作？能否如外界预期的十万小时寿命？此与晶片至灯具的散热息息相关。综观上述各种散热技术，不难发现LED的散热技术日益多元化。应用在高功率LED灯具的散热技术，也不再是单一选择或单一应用。如何巧妙搭配各种散热技术，使其达成低热阻、高功率之LED灯具，為目前LED最重要的课题之一。

（本文作者为阳杰科技处长）