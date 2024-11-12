import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np

class FinanceCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Financial Calculator")
        self.root.geometry("600x400")
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True)
        
        # Create tabs
        self.capm_tab = ttk.Frame(self.notebook)
        self.portfolio_tab = ttk.Frame(self.notebook)
        self.wacc_tab = ttk.Frame(self.notebook)
        self.stock_val_tab = ttk.Frame(self.notebook)
        self.npv_tab = ttk.Frame(self.notebook)
        
        # Add tabs to notebook
        self.notebook.add(self.capm_tab, text="CAPM")
        self.notebook.add(self.portfolio_tab, text="Portfolio")
        self.notebook.add(self.wacc_tab, text="WACC")
        self.notebook.add(self.stock_val_tab, text="Stock Valuation")
        self.notebook.add(self.npv_tab, text="NPV")
        
        # Setup each tab
        self.setup_capm_tab()
        self.setup_portfolio_tab()
        self.setup_wacc_tab()
        self.setup_stock_val_tab()
        self.setup_npv_tab()

    def setup_capm_tab(self):
        ttk.Label(self.capm_tab, text="CAPM Expected Return Calculator", font=('Arial', 12, 'bold')).pack(pady=10)
        frame = ttk.Frame(self.capm_tab)
        frame.pack(pady=10)
        ttk.Label(frame, text="Risk-free Rate (%):").grid(row=0, column=0, padx=5, pady=5)
        self.rf_entry = ttk.Entry(frame)
        self.rf_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(frame, text="Beta:").grid(row=1, column=0, padx=5, pady=5)
        self.beta_entry = ttk.Entry(frame)
        self.beta_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(frame, text="Market Risk Premium (%):").grid(row=2, column=0, padx=5, pady=5)
        self.mrp_entry = ttk.Entry(frame)
        self.mrp_entry.grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(frame, text="Calculate", command=self.calculate_capm).grid(row=3, column=0, columnspan=2, pady=10)
        self.capm_result = ttk.Label(frame, text="")
        self.capm_result.grid(row=4, column=0, columnspan=2, pady=5)

    def setup_portfolio_tab(self):
        ttk.Label(self.portfolio_tab, text="Portfolio Calculator", font=('Arial', 12, 'bold')).pack(pady=10)
        frame = ttk.Frame(self.portfolio_tab)
        frame.pack(pady=10)
        
        # Asset 1 inputs
        ttk.Label(frame, text="Asset 1", font=('Arial', 10, 'bold')).grid(row=0, column=0, columnspan=2, pady=5)
        ttk.Label(frame, text="Expected Return (%):").grid(row=1, column=0, padx=5, pady=5)
        self.asset1_return = ttk.Entry(frame)
        self.asset1_return.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(frame, text="Standard Deviation (%):").grid(row=2, column=0, padx=5, pady=5)
        self.asset1_std = ttk.Entry(frame)
        self.asset1_std.grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(frame, text="Weight (%):").grid(row=3, column=0, padx=5, pady=5)
        self.asset1_weight = ttk.Entry(frame)
        self.asset1_weight.grid(row=3, column=1, padx=5, pady=5)
        
        # Asset 2 inputs
        ttk.Label(frame, text="Asset 2", font=('Arial', 10, 'bold')).grid(row=0, column=2, columnspan=2, pady=5)
        ttk.Label(frame, text="Expected Return (%):").grid(row=1, column=2, padx=5, pady=5)
        self.asset2_return = ttk.Entry(frame)
        self.asset2_return.grid(row=1, column=3, padx=5, pady=5)
        ttk.Label(frame, text="Standard Deviation (%):").grid(row=2, column=2, padx=5, pady=5)
        self.asset2_std = ttk.Entry(frame)
        self.asset2_std.grid(row=2, column=3, padx=5, pady=5)
        ttk.Label(frame, text="Weight (%):").grid(row=3, column=2, padx=5, pady=5)
        self.asset2_weight = ttk.Entry(frame)
        self.asset2_weight.grid(row=3, column=3, padx=5, pady=5)
        
        # Correlation coefficient
        ttk.Label(frame, text="Correlation Coefficient (-1 to 1):").grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.correlation = ttk.Entry(frame)
        self.correlation.grid(row=4, column=2, columnspan=2, padx=5, pady=5)
        
        # Calculate button
        ttk.Button(frame, text="Calculate Portfolio Metrics", command=self.calculate_portfolio).grid(row=5, column=0, columnspan=4, pady=10)
        
        # Results
        self.portfolio_results = ttk.Label(frame, text="", justify=tk.LEFT)
        self.portfolio_results.grid(row=6, column=0, columnspan=4, pady=5)

    def setup_wacc_tab(self):
        ttk.Label(self.wacc_tab, text="WACC Calculator", font=('Arial', 12, 'bold')).pack(pady=10)
        frame = ttk.Frame(self.wacc_tab)
        frame.pack(pady=10)
        ttk.Label(frame, text="Equity Value:").grid(row=0, column=0, padx=5, pady=5)
        self.equity_value_entry = ttk.Entry(frame)
        self.equity_value_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(frame, text="Debt Value:").grid(row=1, column=0, padx=5, pady=5)
        self.debt_value_entry = ttk.Entry(frame)
        self.debt_value_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(frame, text="Cost of Equity (%):").grid(row=2, column=0, padx=5, pady=5)
        self.cost_equity_entry = ttk.Entry(frame)
        self.cost_equity_entry.grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(frame, text="Pre-tax Cost of Debt (%):").grid(row=3, column=0, padx=5, pady=5)
        self.cost_debt_entry = ttk.Entry(frame)
        self.cost_debt_entry.grid(row=3, column=1, padx=5, pady=5)
        ttk.Label(frame, text="Tax Rate (%):").grid(row=4, column=0, padx=5, pady=5)
        self.tax_rate_entry = ttk.Entry(frame)
        self.tax_rate_entry.grid(row=4, column=1, padx=5, pady=5)
        ttk.Button(frame, text="Calculate", command=self.calculate_wacc).grid(row=5, column=0, columnspan=2, pady=10)
        self.wacc_result = ttk.Label(frame, text="")
        self.wacc_result.grid(row=6, column=0, columnspan=2, pady=5)

    def setup_stock_val_tab(self):
        ttk.Label(self.stock_val_tab, text="Stock Valuation Calculator", font=('Arial', 12, 'bold')).pack(pady=10)
        frame = ttk.Frame(self.stock_val_tab)
        frame.pack(pady=10)
        
        # Dividend Discount Model inputs
        ttk.Label(frame, text="Dividend Discount Model", font=('Arial', 10, 'bold')).grid(row=0, column=0, columnspan=2, pady=5)
        ttk.Label(frame, text="Current Dividend:").grid(row=1, column=0, padx=5, pady=5)
        self.current_div = ttk.Entry(frame)
        self.current_div.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Growth Rate (%):").grid(row=2, column=0, padx=5, pady=5)
        self.growth_rate = ttk.Entry(frame)
        self.growth_rate.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Required Return (%):").grid(row=3, column=0, padx=5, pady=5)
        self.req_return = ttk.Entry(frame)
        self.req_return.grid(row=3, column=1, padx=5, pady=5)
        
        # P/E Ratio Valuation inputs
        ttk.Label(frame, text="P/E Ratio Valuation", font=('Arial', 10, 'bold')).grid(row=0, column=2, columnspan=2, pady=5)
        ttk.Label(frame, text="Earnings Per Share:").grid(row=1, column=2, padx=5, pady=5)
        self.eps = ttk.Entry(frame)
        self.eps.grid(row=1, column=3, padx=5, pady=5)
        
        ttk.Label(frame, text="Target P/E Ratio:").grid(row=2, column=2, padx=5, pady=5)
        self.pe_ratio = ttk.Entry(frame)
        self.pe_ratio.grid(row=2, column=3, padx=5, pady=5)
        
        # Calculate buttons
        ttk.Button(frame, text="Calculate DDM Value", command=self.calculate_ddm).grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(frame, text="Calculate P/E Value", command=self.calculate_pe).grid(row=4, column=2, columnspan=2, pady=10)
        
        # Results
        self.ddm_result = ttk.Label(frame, text="")
        self.ddm_result.grid(row=5, column=0, columnspan=2, pady=5)
        self.pe_result = ttk.Label(frame, text="")
        self.pe_result.grid(row=5, column=2, columnspan=2, pady=5)

    def setup_npv_tab(self):
        ttk.Label(self.npv_tab, text="NPV Calculator", font=('Arial', 12, 'bold')).pack(pady=10)
        frame = ttk.Frame(self.npv_tab)
        frame.pack(pady=10)
        ttk.Label(frame, text="Initial Investment:").grid(row=0, column=0, padx=5, pady=5)
        self.investment_entry = ttk.Entry(frame)
        self.investment_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(frame, text="Cash Flows (comma separated):").grid(row=1, column=0, padx=5, pady=5)
        self.cash_flows_entry = ttk.Entry(frame)
        self.cash_flows_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(frame, text="Discount Rate (%):").grid(row=2, column=0, padx=5, pady=5)
        self.discount_rate_entry = ttk.Entry(frame)
        self.discount_rate_entry.grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(frame, text="Calculate NPV", command=self.calculate_npv).grid(row=3, column=0, columnspan=2, pady=10)
        self.npv_result = ttk.Label(frame, text="")
        self.npv_result.grid(row=4, column=0, columnspan=2, pady=5)

    # CAPM Calculation
    def calculate_capm(self):
        try:
            rf = float(self.rf_entry.get()) / 100
            beta = float(self.beta_entry.get())
            mrp = float(self.mrp_entry.get()) / 100
            expected_return = rf + beta * mrp
            self.capm_result.config(text=f"Expected Return: {expected_return*100:.2f}%")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

    # Portfolio Calculation
    def calculate_portfolio(self):
        try:
            r1 = float(self.asset1_return.get()) / 100
            r2 = float(self.asset2_return.get()) / 100
            std1 = float(self.asset1_std.get()) / 100
            std2 = float(self.asset2_std.get()) / 100
            w1 = float(self.asset1_weight.get()) / 100
            w2 = float(self.asset2_weight.get()) / 100
            corr = float(self.correlation.get())
            
            if abs(w1 + w2 - 1) > 0.0001:
                messagebox.showerror("Error", "Weights must sum to 100%")
                return
            
            portfolio_return = w1 * r1 + w2 * r2
            portfolio_variance = (w1**2 * std1**2 + w2**2 * std2**2 + 
                                2 * w1 * w2 * std1 * std2 * corr)
            portfolio_std = np.sqrt(portfolio_variance)
            
            rf = 0.02
            sharpe_ratio = (portfolio_return - rf) / portfolio_std
            
            results_text = (
                f"Portfolio Expected Return: {portfolio_return:.2%}\n"
                f"Portfolio Standard Deviation: {portfolio_std:.2%}\n"
                f"Portfolio Sharpe Ratio: {sharpe_ratio:.2f}\n"
            )
            self.portfolio_results.config(text=results_text)
        
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

    # Stock Valuation: Dividend Discount Model
    def calculate_ddm(self):
        try:
            div = float(self.current_div.get())
            growth = float(self.growth_rate.get()) / 100
            req_return = float(self.req_return.get()) / 100
            stock_price = div * (1 + growth) / (req_return - growth)
            self.ddm_result.config(text=f"DDM Stock Value: ${stock_price:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    # Stock Valuation: P/E Ratio Model
    def calculate_pe(self):
        try:
            eps = float(self.eps.get())
            pe = float(self.pe_ratio.get())
            stock_price = eps * pe
            self.pe_result.config(text=f"P/E Stock Value: ${stock_price:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

    # WACC Calculation
    def calculate_wacc(self):
        try:
            equity_value = float(self.equity_value_entry.get())
            debt_value = float(self.debt_value_entry.get())
            cost_equity = float(self.cost_equity_entry.get()) / 100
            cost_debt = float(self.cost_debt_entry.get()) / 100
            tax_rate = float(self.tax_rate_entry.get()) / 100
            total_value = equity_value + debt_value
            wacc = (equity_value / total_value * cost_equity) + (debt_value / total_value * cost_debt * (1 - tax_rate))
            self.wacc_result.config(text=f"WACC: {wacc * 100:.2f}%")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    # NPV Calculation
    def calculate_npv(self):
        try:
            investment = float(self.investment_entry.get())
            cash_flows = list(map(float, self.cash_flows_entry.get().split(',')))
            discount_rate = float(self.discount_rate_entry.get()) / 100
            npv = -investment
            for i, cash_flow in enumerate(cash_flows):
                npv += cash_flow / (1 + discount_rate) ** (i + 1)
            self.npv_result.config(text=f"NPV: ${npv:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

def main():
    root = tk.Tk()
    app = FinanceCalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
