-- 품종 장미
select
  saleDate as '거래일자',
  goodName as '상품명',
  cast(avg(avgAMT) as int) as '평균가격'
from
  query_7
where
  pumName == '장미'
group by goodName;

-- 품종 유칼립투스
select
  saleDate as '거래일자',
  goodName as '상품명',
  cast(avg(avgAMT) as int) as '평균가격'
from
  query_7
where
  pumName == '유칼립투스'
group by goodName;

-- 품종 라넌큘러스
select
  saleDate as '거래일자',
  goodName as '상품명',
  cast(avg(avgAMT) as int) as '평균가격'
from
  query_7
where
  pumName == '라넌큘러스'
group by goodName;