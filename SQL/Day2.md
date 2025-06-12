
A window function is a special type of function in SQL or data analysis tools that performs calculations across a set of rows related to the current row. The key thing to understand is that it lets you perform calculations while keeping the "window" of rows around the current row in focus.

### Example
Imagine you have a list of sales for each day of the week, and you want to calculate the average sales for the current day and the two previous days (a "window" of 3 days). The window function would allow you to calculate this average without having to group the rows or lose the detail of each individual day

## Variations of Window Functions

ROW_NUMBER(): This assigns a unique number to each row, based on the specified order. It’s like numbering the rows in a sequence.

RANK(): Similar to ROW_NUMBER(), but if two rows have the same value, they get the same rank, and the next rank is skipped.

DENSE_RANK(): Like RANK(), but it doesn't skip any ranks. For example, if two rows are tied for rank 1, the next row will be rank 2.

NTILE(n): Divides the rows into n equal groups (or as equal as possible) and assigns a group number to each row.

LEAD() and LAG(): These functions allow you to look at the next (LEAD) or previous (LAG) row's value in the result set, useful for comparisons.

SUM() / AVG() / MIN() / MAX(): These aggregate functions can be used as window functions, allowing you to calculate running totals, averages, and more, without collapsing your data into one row.

FIRST_VALUE() / LAST_VALUE(): These functions let you get the first or last value in the window.



Sure! Let’s break down each variation of window functions with a practical example using a simple sales dataset:

### 1. **ROW\_NUMBER()**

Assigns a unique number to each row, based on the specified order.

**Use case**: You want to rank rows in a specific order, like ranking employees by their sales.

#### Example:

```sql
SELECT 
    Employee,
    Sales,
    ROW_NUMBER() OVER (ORDER BY Sales DESC) AS Sales_Rank
FROM EmployeeSales;
```

**Explanation**: This query ranks employees based on their sales (highest to lowest).

**Output**:

| Employee | Sales | Sales\_Rank |
| -------- | ----- | ----------- |
| Alice    | 500   | 1           |
| Bob      | 450   | 2           |
| Carol    | 400   | 3           |
| Dave     | 350   | 4           |

---

### 2. **RANK()**

Similar to `ROW_NUMBER()`, but if two rows have the same value, they get the same rank, and the next rank is skipped.

**Use case**: You want to rank students by their scores but handle ties.

#### Example:

```sql
SELECT 
    Student,
    Score,
    RANK() OVER (ORDER BY Score DESC) AS Rank
FROM StudentScores;
```

**Explanation**: This query ranks students by score, but if two students have the same score, they receive the same rank.

**Output**:

| Student | Score | Rank |
| ------- | ----- | ---- |
| John    | 95    | 1    |
| Jane    | 95    | 1    |
| Alice   | 90    | 3    |
| Bob     | 85    | 4    |

---

### 3. **DENSE\_RANK()**

Similar to `RANK()`, but no ranks are skipped. If two rows tie for a rank, the next rank will still be the next consecutive number.

**Use case**: You want to rank runners in a race, where no rank should be skipped even if there are ties.

#### Example:

```sql
SELECT 
    Runner,
    Time,
    DENSE_RANK() OVER (ORDER BY Time ASC) AS Race_Rank
FROM RaceResults;
```

**Explanation**: This query assigns ranks to runners based on their time (ascending order), and no ranks will be skipped if there’s a tie.

**Output**:

| Runner | Time | Race\_Rank |
| ------ | ---- | ---------- |
| Alice  | 5.2  | 1          |
| Bob    | 5.4  | 2          |
| Carol  | 5.4  | 2          |
| Dave   | 5.7  | 3          |

---

### 4. **NTILE(n)**

Divides the data into `n` equal groups and assigns a group number to each row.

**Use case**: You want to divide employees into 4 performance quartiles based on their sales.

#### Example:

```sql
SELECT 
    Employee,
    Sales,
    NTILE(4) OVER (ORDER BY Sales DESC) AS Quartile
FROM EmployeeSales;
```

**Explanation**: This query divides the employees into 4 quartiles based on their sales (highest sales get 1st quartile).

**Output**:

| Employee | Sales | Quartile |
| -------- | ----- | -------- |
| Alice    | 500   | 1        |
| Bob      | 450   | 1        |
| Carol    | 400   | 2        |
| Dave     | 350   | 3        |

---

### 5. **LEAD()**

Allows you to look at the next row's value in the result set.

**Use case**: You want to compare each day's sales with the next day's sales.

#### Example:

```sql
SELECT 
    Date,
    Sales,
    LEAD(Sales) OVER (ORDER BY Date) AS Next_Day_Sales
FROM SalesData;
```

**Explanation**: This query shows each day’s sales along with the sales for the next day.

**Output**:

| Date       | Sales | Next\_Day\_Sales |
| ---------- | ----- | ---------------- |
| 2025-06-01 | 200   | 220              |
| 2025-06-02 | 220   | 210              |
| 2025-06-03 | 210   | 250              |
| 2025-06-04 | 250   | NULL             |

---

### 6. **LAG()**

Allows you to look at the previous row's value in the result set.

**Use case**: You want to compare each day's sales with the previous day's sales.

#### Example:

```sql
SELECT 
    Date,
    Sales,
    LAG(Sales) OVER (ORDER BY Date) AS Previous_Day_Sales
FROM SalesData;
```

**Explanation**: This query shows each day's sales along with the sales for the previous day.

**Output**:

| Date       | Sales | Previous\_Day\_Sales |
| ---------- | ----- | -------------------- |
| 2025-06-01 | 200   | NULL                 |
| 2025-06-02 | 220   | 200                  |
| 2025-06-03 | 210   | 220                  |
| 2025-06-04 | 250   | 210                  |

---

### 7. **SUM() / AVG() / MIN() / MAX()**

These aggregate functions can be used as window functions to perform calculations over a specified window of data.

**Use case**: You want to calculate the moving average of sales for each day.

#### Example:

```sql
SELECT 
    Date,
    Sales,
    AVG(Sales) OVER (ORDER BY Date ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS Moving_Avg
FROM SalesData;
```

**Explanation**: This query calculates a 3-day moving average (previous, current, and next day’s sales) for each day.

**Output**:

| Date       | Sales | Moving\_Avg |
| ---------- | ----- | ----------- |
| 2025-06-01 | 200   | 210         |
| 2025-06-02 | 220   | 210         |
| 2025-06-03 | 210   | 220         |
| 2025-06-04 | 250   | 220         |

---

### 8. **FIRST\_VALUE() / LAST\_VALUE()**

These functions let you get the first or last value in the window.

**Use case**: You want to know the first and last sale for each month.

#### Example:

```sql
SELECT 
    Month,
    Sales,
    FIRST_VALUE(Sales) OVER (PARTITION BY Month ORDER BY Date) AS First_Sale,
    LAST_VALUE(Sales) OVER (PARTITION BY Month ORDER BY Date ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS Last_Sale
FROM MonthlySales;
```

**Explanation**: This query finds the first and last sale for each month.

**Output**:

| Month      | Sales | First\_Sale | Last\_Sale |
| ---------- | ----- | ----------- | ---------- |
| 2025-06-01 | 200   | 200         | 250        |
| 2025-06-02 | 220   | 200         | 250        |
| 2025-06-03 | 210   | 200         | 250        |
| 2025-06-04 | 250   | 200         | 250        |

---

### Summary:

* **ROW\_NUMBER()**: Assigns a unique number to each row.
* **RANK()**: Assigns ranks but skips ranks in case of ties.
* **DENSE\_RANK()**: Assigns ranks without skipping any in case of ties.
* **NTILE(n)**: Divides the data into `n` equal groups.
* **LEAD()**: Accesses the next row's value.
* **LAG()**: Accesses the previous row's value.
* **SUM() / AVG() / MIN() / MAX()**: Aggregates data over a window.
* **FIRST\_VALUE() / LAST\_VALUE()**: Gets the first or last value in a window.



**list of SQL Window Function practice interview questions**
---

## 🟢 Beginner  Level – Fundamentals

### 📘 Conceptual

1. What is a window function in SQL?
2. How is a window function different from aggregate functions?
3. What does the `OVER()` clause do?
4. Explain `PARTITION BY` vs `GROUP BY`.
5. What are common window functions?

   *(Examples: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE()`, `LEAD()`, `LAG()`, `SUM() OVER`, `AVG() OVER`)*

### 🧪 Practical

6. Write a query using `ROW_NUMBER()` to assign a unique row number to each record.
7. Use `RANK()` to rank employees by salary within each department.
8. Use `DENSE_RANK()` to handle ties in scores.
9. Use `NTILE(4)` to divide a list of students into quartiles based on their GPA.
10. Show previous and next salary using `LAG()` and `LEAD()`.

---

## 🟡 Intermediate Level – Business Logic Scenarios

### 🧩 Real-World Queries

11. Get the top 3 highest-paid employees in each department.
12. Calculate the running total of sales for each salesperson.
13. Compare each day’s sales with the previous day (daily difference).
14. Identify consecutive days where a user logged in (using `LAG()`).
15. Calculate the moving average of sales for the last 3 days.

### 🔧 Edge Cases

16. What happens when you don’t use `PARTITION BY` in a window function?
17. How does sorting in `ORDER BY` inside `OVER()` affect results?
18. Difference between filtering results with `WHERE` vs `QUALIFY` (e.g., in Snowflake, BigQuery).

---

## 🔴 Advanced (Hero) Level – Optimization & Nested Queries

### 💼 Advanced Scenarios

19. Write a query to detect the first and last purchase made by each customer.
20. Calculate the percentage contribution of each sale to total monthly sales using `SUM() OVER()`.
21. Find employees who earn more than the average salary of their department (using windowed `AVG()`).
22. Identify sessions of users with gaps in activity (e.g., >30 mins difference using `LAG()`).
23. Find the longest streak of increasing stock prices using window functions.

### 🧠 Complex Logic

24. Rank products based on sales within rolling 3-month windows.
25. Calculate cumulative distinct count using `COUNT(DISTINCT)` logic with windows.
26. Combine window functions with CTEs or subqueries to perform layered analysis.

---

## 🔁 Bonus: Challenge Questions

### 💡 Challenge 1

> **Problem:** For each user, find the second most recent login date.

```sql
SELECT *
FROM (
  SELECT user_id, login_date,
         ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date DESC) as rn
  FROM logins
) t
WHERE rn = 2;
```

### 💡 Challenge 2

> **Problem:** Detect “duplicate” rows with same values but different IDs.


