{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "857e979a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your annual salary200000\n",
      "Enter the percent of your salary to save, as a decimal0.2\n",
      "Enter the cost of your dream home500000\n",
      "37\n"
     ]
    }
   ],
   "source": [
    "#PartA\n",
    "\n",
    "#Salary and current savings per year\n",
    "annual_salary = int(input(\"Enter your annual salary\"))\n",
    "monthly_salary= annual_salary/12\n",
    "\n",
    "#Every month your current savings will accumilate as you earn a monthly salary.\n",
    "current_savings = 0 + monthly_salary\n",
    "#You invest your current savings and recive a return every month which is added to your current savings.\n",
    "monthly_return= current_savings * 0.04/12\n",
    "current_savings2= current_savings + monthly_return\n",
    "\n",
    "#You are still saving for the house which is the percentage saved\n",
    "#Part of your current savings togther with your investment is taken to calculate your portion\n",
    "amount_percentage = float(input(\"Enter the percent of your salary to save, as a decimal\"))\n",
    "portion_saved =(current_savings2 * amount_percentage)\n",
    "\n",
    "#Total amount of the house and the downpayment needed to secure it.\n",
    "total_cost= int(input(\"Enter the cost of your dream home\"))\n",
    "portion_down_payment= (0.25 * total_cost)\n",
    "\n",
    "# if one month you save a portion how many months will it take for you to reach total cost?\n",
    "Number_of_months =int((portion_down_payment*1)/portion_saved)\n",
    "print(Number_of_months,\"months to save for the downpayment of your dream home\")                      \n",
    "                      \n",
    "                      \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3379976",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
