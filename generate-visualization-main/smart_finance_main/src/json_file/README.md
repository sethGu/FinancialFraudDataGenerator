#### store_generate_ratio 表示在构建商户的过程中选择好大类后每个子类的概率
#### store_rank_classes 表示每个大类商户拥有的低中高三个等级的商户子类有哪些
#### store_consume_section 表示每个子类商户消费区间
#### consume_subclass_ratio 表示每个子类对于不同消费者的消费概率是多少，其中list里面的顺序与store_generate_ratio一致
#### exist_three_rank_consume_ratio 表示子类存在低中高三个等级的商户，用户消费时选择某类等级的概率，list里面的顺序为低、中、高
#### store_open_time 表示每类商户的营业时间（不区分低中高三个等级）