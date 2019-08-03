defmodule Time do

  # months_30 -> months with 30 days
  def months_30(n, years, months, days) do
    # 364*119 = 43316 days from 1900-2019
    IO.puts ("#{months}, #{days} , #{years}")

    # n here sets number of times loop should run, needs to be in every time fn
    # alternative would be to have nStart, nStop, if nStart == nStop, exit
    # too many params tho
    if n == 1000 do
      exit(:shutdown)
    end

    # if n % 364 == 0 do
    if rem(n,364) == 0 do
      # start in Jan next year, 31 days -> months_31
      month_Jan(n+1, years+1, 1, 1)
    end

    if years == 2019 and months == 12 and days == 31 do
      years = 1900
    end

    # 30*5+28+31*6 = 364
    if days == 30 do
      months_31(n+1, years, months+1, 1)
    end

    months_30(n+1, years, months, days+1)
  end

  # months with 31 days
  def months_31(n, years, months, days) do
    # 364*119 = 43316 days from 1900-2019
    IO.puts ("#{months}, #{days} , #{years}")

    # n here sets number of times loop should run, needs to be in every time fn
    if n == 1000 do
      exit(:shutdown)
    end

    # 30*5+28+31*6 = 364
    if days == 31 do
      months_30(n+1, years, months+1, 1)
    end

    if rem(n,364) == 0 do
      month_Jan(n+1, years+1, 1, 1)
    end

    if years == 2019 and months == 12 and days == 31 do
      years = 1900
    end

    months_31(n+1, years, months, days+1)
  end

  #handle feb, 
  #month with 28 days
  #then call March, 31 days, fn months_31
  def month_Feb(n, years, months, days) do
    # 364*119 = 43316 days from 1900-2019, which is irrelevant
    IO.puts ("#{months}, #{days} , #{years}")

    # n here sets number of times loop should run, needs to be in every time fn
    if n == 1000 do
      exit(:shutdown)
    end

    # if n % 364 == 0 do
    if rem(n,364) == 0 do
      month_Jan(n, years+1, 1, 1)
    end

    if years == 2019 and months == 12 and days == 31 do
      years = 1900
    end

    if months == 12 and days == 31 do
      #dec 31, call January -> fn month_Jan
      month_Jan(n+1,years+1,1,1)
    end

    # 30*5+28+31*6 = 364
    if days == 28 do
      months_31(n+1, years, months+1, 1)
      # go to April, 31 days -> fn months_31
    end

    if years == 2019 and months == 12 and days == 31 do
      years = 1900
    end

    month_Feb(n+1, years, months, days+1)
  end

# january, call February -> fn month_Feb
def month_Jan(n, years, months, days) do
    # 364*119 = 43316 days from 1900-2019
    IO.puts ("#{months}, #{days} , #{years}")
    
    if n == 1000 do
      exit(:shutdown)
    end

    # if n % 364 == 0 do
    if rem(n,364) == 0 do
      month_Jan(n+1, years+1, 1, 1)
    end

    if years == 2019 and months == 12 and days == 31 do
      years = 1900
    end

    if days == 31 do
      month_Feb(n+1, years, months+1, 1)
    end

    month_Jan(n+1, years, months, days+1)
  end

end
#endtime
IO.puts ("Mos,Days,Years")
Time.month_Jan(1,1900,1,1)
# DEBUG?
  # ignore months because need to go through december... debug?!