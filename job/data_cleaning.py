isTest = True
area_data = {
            '北京': ['北京','朝阳区', '海淀区', '通州区', '房山区', '丰台区', '昌平区', '大兴区', '顺义区', '西城区', '延庆县', '石景山区', '宣武区', '怀柔区', '崇文区', '密云县',
                '东城区', '门头沟区', '平谷区'],
            '广东':['广东省', '东莞', '广州', '中山', '深圳', '惠州', '江门', '珠海', '汕头', '佛山', '湛江', '河源', '肇庆','潮州', '清远', '韶关', '揭阳', '阳江', '云浮', '茂名', '梅州', '汕尾'],
            '山东':['山东省', '济南', '青岛', '临沂', '济宁', '菏泽', '烟台','泰安', '淄博', '潍坊', '日照', '威海', '滨州', '东营', '聊城', '德州', '莱芜', '枣庄'],
            '江苏':['江苏省', '苏州', '徐州', '盐城', '无锡','南京', '南通', '连云港', '常州', '扬州', '镇江', '淮安', '泰州', '宿迁'],
            '河南':['河南省', '郑州', '南阳', '新乡', '安阳', '洛阳', '信阳','平顶山', '周口', '商丘', '开封', '焦作', '驻马店', '濮阳', '三门峡', '漯河', '许昌', '鹤壁', '济源'],
            '上海':['上海', '松江区', '宝山区', '金山区','嘉定区', '南汇区', '青浦区', '浦东新区', '奉贤区', '闵行区', '徐汇区', '静安区', '黄浦区', '普陀区', '杨浦区', '虹口区', '闸北区', '长宁区', '崇明县', '卢湾区'],
            '河北':[ '河北省', '石家庄', '唐山', '保定', '邯郸', '邢台', '河北区', '沧州', '秦皇岛', '张家口', '衡水', '廊坊', '承德'],
            '浙江':['浙江省', '温州', '宁波','杭州', '台州', '嘉兴', '金华', '湖州', '绍兴', '舟山', '丽水', '衢州'],
            '陕西':['陕西省', '西安', '咸阳', '宝鸡', '汉中', '渭南','安康', '榆林', '商洛', '延安', '铜川'],
            '湖南':[ '湖南省', '长沙', '邵阳', '常德', '衡阳', '株洲', '湘潭', '永州', '岳阳', '怀化', '郴州','娄底', '益阳', '张家界', '湘西州'],
            '重庆':[  '重庆', '江北区', '渝北区', '沙坪坝区', '九龙坡区', '万州区', '永川', '南岸区', '酉阳县', '北碚区', '涪陵区', '秀山县', '巴南区', '渝中区', '石柱县', '忠县', '合川', '大渡口区', '开县', '长寿区', '荣昌县', '云阳县', '梁平县', '潼南县', '江津', '彭水县', '璧山县', '綦江县',
        '大足县', '黔江区', '巫溪县', '巫山县', '垫江县', '丰都县', '武隆县', '万盛区', '铜梁县', '南川', '奉节县', '双桥区', '城口县'],
            '福建':['福建省', '漳州', '泉州','厦门', '福州', '莆田', '宁德', '三明', '南平', '龙岩'],
            '天津':['天津', '和平区', '北辰区', '河北区', '河西区', '西青区', '津南区', '东丽区', '武清区','宝坻区', '红桥区', '大港区', '汉沽区', '静海县', '宁河县', '塘沽区', '蓟县', '南开区', '河东区'],
            '云南':[ '云南省', '昆明', '红河州', '大理州', '文山州', '德宏州', '曲靖', '昭通', '楚雄州', '保山', '玉溪', '丽江地区', '临沧地区', '思茅地区', '西双版纳州', '怒江州', '迪庆州'],
            '四川':['四川省', '成都', '绵阳', '广元','达州', '南充', '德阳', '广安', '阿坝州', '巴中', '遂宁', '内江', '凉山州', '攀枝花', '乐山', '自贡', '泸州', '雅安', '宜宾', '资阳','眉山', '甘孜州'],
            '广西':['广西壮族自治区', '贵港', '玉林', '北海', '南宁', '柳州', '桂林', '梧州', '钦州', '来宾', '河池', '百色', '贺州', '崇左',  '防城港'],
            '安徽':['安徽省', '芜湖', '合肥', '六安', '宿州', '阜阳','安庆', '马鞍山', '蚌埠', '淮北', '淮南', '宣城', '黄山', '铜陵', '亳州','池州', '巢湖', '滁州'],
            '海南':['海南省', '三亚', '海口', '琼海', '文昌', '东方', '昌江县', '陵水县', '乐东县', '五指山', '保亭县', '澄迈县', '万宁','儋州', '临高县', '白沙县', '定安县', '琼中县', '屯昌县'],
            '江西':['江西省', '南昌', '赣州', '上饶', '吉安', '九江', '新余', '抚州', '宜春', '景德镇', '萍乡', '鹰潭'],
            '湖北':['湖北省', '武汉', '宜昌', '襄樊', '荆州', '恩施州', '孝感', '黄冈', '十堰', '咸宁', '黄石', '仙桃', '随州', '天门', '荆门', '潜江', '鄂州', '神农架林区'],
            '山西':['山西省', '太原', '大同', '运城', '长治', '晋城', '忻州', '临汾', '吕梁', '晋中', '阳泉', '朔州'],
            '辽宁':['辽宁省', '大连', '沈阳', '丹东', '辽阳', '葫芦岛', '锦州', '朝阳', '营口', '鞍山', '抚顺', '阜新', '本溪', '盘锦', '铁岭'],
            '台湾':['台湾省','台北', '高雄', '台中', '新竹', '基隆', '台南', '嘉义'],
            '黑龙江':['黑龙江', '齐齐哈尔', '哈尔滨', '大庆', '佳木斯', '双鸭山', '牡丹江', '鸡西','黑河', '绥化', '鹤岗', '伊春', '大兴安岭地区', '七台河'],
            '内蒙古':['内蒙古自治区', '赤峰', '包头', '通辽', '呼和浩特', '乌海', '鄂尔多斯', '呼伦贝尔','兴安盟', '巴彦淖尔盟', '乌兰察布盟', '锡林郭勒盟', '阿拉善盟'],
            '香港':["香港","香港特别行政区"],
            '澳门':['澳门','澳门特别行政区'],
            '贵州':['贵州省', '贵阳', '黔东南州', '黔南州', '遵义', '黔西南州', '毕节地区', '铜仁地区','安顺', '六盘水'],
            '甘肃':['甘肃省', '兰州', '天水', '庆阳', '武威', '酒泉', '张掖', '陇南地区', '白银', '定西地区', '平凉', '嘉峪关', '临夏回族自治州','金昌', '甘南州'],
            '青海':['青海省', '西宁', '海西州', '海东地区', '海北州', '果洛州', '玉树州', '黄南藏族自治州'],
            '新疆':['新疆','新疆维吾尔自治区', '乌鲁木齐', '伊犁州', '昌吉州','石河子', '哈密地区', '阿克苏地区', '巴音郭楞州', '喀什地区', '塔城地区', '克拉玛依', '和田地区', '阿勒泰州', '吐鲁番地区', '阿拉尔', '博尔塔拉州', '五家渠',
        '克孜勒苏州', '图木舒克'],
            '西藏':['西藏区', '拉萨', '山南地区', '林芝地区', '日喀则地区', '阿里地区', '昌都地区', '那曲地区'],
            '吉林':['吉林省', '吉林', '长春', '白山', '白城','延边州', '松原', '辽源', '通化', '四平'],
            '宁夏':['宁夏回族自治区', '银川', '吴忠', '中卫', '石嘴山', '固原']
        }


import re

def modifyType(item, allTag):
    if 'avascript' in allTag:
        item['Jtype'] = 'IT·互联网_技术_前端_Javascript'
    elif 'ava' in allTag:
        item['Jtype'] = 'IT·互联网_技术_开发_Java'
        
    elif 'ython' in allTag:
        item['Jtype'] = 'IT·互联网_技术_开发_Python'

    elif '++' in allTag:
        item['Jtype'] = 'IT·互联网_技术_开发_C++'

    elif 'C#' in allTag or 'c#' in allTag:
        item['Jtype'] = 'IT·互联网_技术_开发_C#'
    
    elif '.net' in allTag or '.NET' in allTag:
        item['Jtype'] = 'IT·互联网_技术_开发_.NET'
    
    elif 'SQL' in allTag or 'sql' in allTag:
        item['Jtype'] = 'IT·互联网_技术_开发_SQL'
    elif 'Swift' in allTag or 'swift' in allTag:
        item['Jtype'] = 'IT·互联网_技术_开发_Swift'
    elif 'Ruby' in allTag or 'ruby' in allTag:
        item['Jtype'] = 'IT·互联网_技术_开发_Ruby'
    elif 'Rust' in allTag or 'rust' in allTag:
        item['Jtype'] = 'IT·互联网_技术_开发_Rust'
    elif 'Go' in allTag or 'go' in allTag:
        item['Jtype'] = 'IT·互联网_技术_开发_Go'
    elif 'PHP' in allTag or 'Php' in allTag or 'php' in allTag:
        item['Jtype'] = 'IT·互联网_技术_开发_PHP'
    elif 'iOS' in allTag or 'ios' in allTag or 'IOS' in allTag:
        item['Jtype'] = 'IT·互联网_技术_移动开发_iOS'

    elif 'ndroid' in allTag or '安卓' in allTag:
        item['Jtype'] = 'IT·互联网_技术_移动开发_Android'
    elif '大数据' in allTag:
        item['Jtype'] = 'IT·互联网_技术_开发_大数据'

    elif '推荐' in allTag:
        item['Jtype'] = 'IT·互联网_技术_开发_推荐算法'

    elif '前端' in allTag:
        item['Jtype'] = 'IT·互联网_技术_前端'

    elif 'HTML5' in allTag or 'html5' in allTag:
        item['Jtype'] = 'IT·互联网_技术_前端_HTML5'

    elif 'Web' in allTag or 'web' in allTag:
        item['Jtype'] = 'IT·互联网_技术_前端_Web'

    elif '测试' in allTag:
        item['Jtype'] = 'IT·互联网_技术_测试'

    elif '运维' in allTag or '系统工程师' in allTag or '网络工程师' in allTag or 'DBA' in allTag:
        item['Jtype'] = 'IT·互联网_技术_运维'

    elif '技术经理' in allTag or '架构师' in allTag or '技术总监' in allTag or 'CTO' in allTag or '安全专家' in allTag or '项目总监' in allTag:
        item['Jtype'] = 'IT·互联网_技术_高端职位'

    elif 'AI产品' in allTag or '物流产品' in allTag or '网页产品' in allTag or '移动产品' in allTag or '数据产品' in allTag or '电商产品' in allTag or '游戏策划' in allTag or '游戏制作人' in allTag:
        item['Jtype'] = 'IT·互联网_产品'
    
    elif 'UI设计' in allTag or '视觉设计' in allTag or '网页设计' in allTag or 'APP设计' in allTag or '平面设计' in allTag or '动作设计' in allTag or '美术设计' in allTag or '广告设计' in allTag or '多媒体设计' in allTag or '广告设计' in allTag or '游戏角色' in allTag or '游戏动作' in allTag or '游戏设计' in allTag:
        item['Jtype'] = 'IT·互联网_设计'

    elif '运营' in allTag or '主编' in allTag or '副主编' in allTag or '编辑' in allTag or '文案策划' in allTag or '记者' in allTag or '网络推广' in allTag or '淘宝客服' in allTag or '客服经理' in allTag or '客服总监' in allTag or 'COO' in allTag:
        item['Jtype'] = 'IT·互联网_运营'
    
    elif '互联网' in allTag or '算法' in allTag or '电商' in allTag or '程序员' in allTag or '软件开发' in allTag or '网络优化' in allTag:
        item['Jtype'] = 'IT·互联网'

    # 房地产
    elif '房地产' in allTag or '建筑' in allTag or '建筑工程师' in allTag or '机电工程师' in allTag or '土建工程师' in allTag or '水电工程师' in allTag or '质检工程师' in allTag or '材料总管' in allTag or '结构设计师' in allTag or '钢结构设计' in allTag or '电气设计' in allTag or '暖通设计' in allTag or '给排水设计' in allTag or '室内设计' in allTag or 'CAD' in allTag or '物业' in allTag or '装潢设计' in allTag  or '政设计' in allTag or '房产' in allTag or '房' in allTag or '售楼' in allTag or '造价' in allTag:
        item['Jtype'] = '房地产'

    # 金融
    elif '银行' in allTag or '柜员' in allTag or '理财经理' in allTag or '零售客户经理' in allTag or '支行' in allTag or '行长' in allTag or '风险经理' in allTag or '投资银行' in allTag or 'Teller' in allTag:
        item['Jtype'] = '金融_银行'

    elif '保险' in allTag or '资产' in allTag or '理财' in allTag or '储备主管' in allTag :
        item['Jtype'] = '金融_保险'

    elif '证券' in allTag or '资产' in allTag or '基金' in allTag or '行业研究员' in allTag :
        item['Jtype'] = '金融_证券/基金'

    elif '担保业务' in allTag or '拍卖师' in allTag or '珠宝鉴定' in allTag or '收藏物鉴定' in allTag or 'CFO' in allTag or '财务总监' in allTag or '税务经理' in allTag :
        item['Jtype'] = '金融_其他金融服务'

    elif '金融' in allTag or '出纳' in allTag or '会计' in allTag or '审计' in allTag:
        item['Jtype'] = '金融'


    # 汽车·制造
    elif '汽车制造' in allTag or '底盘' in allTag or '汽车零部件' in allTag or '操作工' in allTag:
        item['Jtype'] = '汽车_汽车制造'

    elif '汽车销售' in allTag:
        item['Jtype'] = '汽车_营销及销售'
    
    elif '汽车' in allTag:
        item['Jtype'] = '汽车'
    #医疗

    elif '医生' in allTag or '护士' in allTag or '药剂师' in allTag:
        item['Jtype'] = '医疗_人员'


    elif '医疗' in allTag or '药品' in allTag or '生物' in allTag:
        item['Jtype'] = '医疗_药品/生物制剂'

    
    #化工
    elif '新材料' in allTag or '新能源' in allTag:
        item['Jtype'] = '化工_新材料/环保技术'
    
    elif '机械' in allTag or '钳工' in allTag or '焊工' in allTag:
        item['Jtype'] = '化工_机械'

    elif '石油' in allTag or '天然气' in allTag:
        item['Jtype'] = '化工_石化'
    
    elif '半导体' in allTag or '集成电路' in allTag:
        item['Jtype'] = '化工_电子'
        
    #文娱
    elif '主播' in allTag or '艺人' in allTag or '歌手' in allTag or '文娱' in allTag:
        item['Jtype'] = '文娱'
        
    #交通运输
    elif '司机' in allTag or '乘务员' in allTag or '机长' in allTag or '空姐' in allTag or '地勤' in allTag or '地铁' in allTag or '火车' in allTag:
        item['Jtype'] = '交通运输'
        
    #服务业
    elif '送餐员' in allTag or '厨师' in allTag or '洗盘' in allTag or '服务员' in allTag or '洗碗' in allTag or '厨' in allTag or '食品' in allTag:
        item['Jtype'] = '服务业_食品'

    elif '顺丰' in allTag or '快递员' in allTag or '菜鸟裹裹' in allTag or '分拣员' in allTag or '物流' in allTag:
        item['Jtype'] = '服务业_物流'
        
    elif '旅游' in allTag:
        item['Jtype'] = '服务业_旅游'

    elif '美甲师' in allTag or '清洁工' in allTag or '扫地' in allTag or '美容师' in allTag or '保安' in allTag or '电话客服' in allTag or '足疗师' in allTag or '教练' in allTag or '网管' in allTag  or '管家' in allTag or '店员' in allTag or '店长' in allTag:
        item['Jtype'] = '服务业'

    #教育业
    elif '老师' in allTag or '教师' in allTag or '教授' in allTag or '招生' in allTag or '课程' in allTag or '教育' in allTag:
        item['Jtype'] = '教育业'
    
    #新闻
    elif '新闻' in allTag or '出版' in allTag:
        item['Jtype'] = '新闻_出版' 

def clean(item):
    #TODO
    Jname0 = ''
    Jtype0 = ''
    Jtag0 = ''
    try :
        Jname0 = item['Jname']
    except:
        pass
    try:
        Jtype0 = item['Jtype']
    except:
        pass
    try:
        Jtag0 = item['Jtag']
    except:
        pass
    allTag = Jname0
    modifyType(item,allTag)
    # IT·互联网
    try:
        if item['Jtype'] == Jtype0:
            allTag = Jname0 + Jtype0
            modifyType(item,allTag)
        
        if item['Jtype'] == Jtype0:
            allTag = Jname0 + Jtype0 + Jtag0
            modifyType(item,allTag)
        
        if item['Jtype'] == Jtype0:
            item['Jtype'] = '其它'
    except:
        pass

    item['Jname'] = Jname0.split('(')[0].split('-')[0]

    #城市划分省

    Jarea0 = ''
    try :
        Jarea0 = item['Jarea']
    except:
        pass
    JareaFinal = ''


    # if '-' not in Jarea0:
    #     for k,v in area_data.items():
    #         for i in v:
    #             if Jarea0 in i:
    #                 item['Jarea'] = k + '-' + Jarea0

    if ',' not in Jarea0:
        if '-' not in Jarea0:
            for k,v in area_data.items():
                for i in v:
                    if Jarea0 in i:
                        JareaFinal = k + '-' + Jarea0
        else :
            JareaFinal = Jarea0.rstrip('-')

    else :
        # JareaNum = len(Jarea0.split(','))
        for JareaEach in (Jarea0.split(',')):
            if '-' not in JareaEach:
                for k,v in area_data.items():
                    for i in v:
                        if JareaEach in i:
                            JareaFinal = JareaFinal + ',' + k + '-' + JareaEach
                            JareaFinal = JareaFinal.lstrip(',')
            else :
                JareaFinal = JareaFinal + ',' + JareaEach
                JareaFinal = JareaFinal.lstrip(',')
    
    item['Jarea'] = JareaFinal


    Jexperience0 = ''
    try:
        Jexperience0 = item['Jexperience']

        if Jexperience0 == '不限':
            item['Jexperience'] = '0'

        if re.search(r'[^\x20-\x7e]', Jexperience0) != None:
            item['Jexperience'] = '0'
    except:
        pass


    try:
        JcomSize0 = item['JcomSize']
        item['JcomSize'] = re.sub(r'[^\x00-\x7F]+','', JcomSize0)
        if re.search(r'[^\x20-\x7e]', item['JhireCount']) != None:
            item['JhireCount'] = '0'
    except:
        pass

    try:
        Jeducation0 = '无'
        for x in ['初中', '高中', '大专', '本科', '硕士']:
            if x in item['Jeducation']:
                Jeducation0 = x
        item['Jeducation'] = Jeducation0
    except:
        pass

    JcomType0 = ''
    # 公司性质
    try:
        JcomType0 = item['JcomType']
    except:
        pass
    if '国有' in JcomType0:
        item['JcomType'] = '国有企业'

    elif '集体' in JcomType0:
        item['JcomType'] = '集体企业'
    
    elif '私营' in JcomType0 or '民营' in JcomType0:
        item['JcomType'] = '私营企业'

    elif '个体' in JcomType0:
        item['JcomType'] = '个体工商户'

    elif '合伙' in JcomType0:
        item['JcomType'] = '合伙企业'
    
    elif '联营' in JcomType0:
        item['JcomType'] = '联营企业'

    elif '股份合作' in JcomType0:
        item['JcomType'] = '股份合作制企业'

    elif '有限责任' in JcomType0:
        item['JcomType'] = '有限责任公司'

    elif '股份有限' in JcomType0:
        item['JcomType'] = '股份有限公司'
    
    else :
        item['JcomType'] = '其他'



    print("经过clean")
    print(item)
    return item





    
 
# for k,v in area_data.items():
#     for i in v:
#         if cityName in i:
#              print(k)

# item['Jtype'] = sp(item['Jtype'])

# def sp(name,type,tag,):
#     """
#     val是传进来的Jtype的原始内容
#     """
#     res = ''
#     if '互联网' in val:
#         res += 'IT互联网'
#     if '技术' in val:
#         res += '_'
#         res += '技术'
#     if 'x' in val:
#         res += '_'
#     return res