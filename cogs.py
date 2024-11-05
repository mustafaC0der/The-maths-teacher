import discord
from discord.ext import commands
from sympy import symbols, Eq, solve

class MathCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="calc")
    async def calculate(self, ctx, *, expression: str):
        """Calculates a simple math expression."""
        try:
            result = eval(expression)
            await ctx.send(f"The result of `{expression}` is `{result}`.")
        except Exception as e:
            await ctx.send("There was an error with your expression.")

    @commands.command(name="solve")
    async def solve_equation(self, ctx, *, equation: str):
        """Solves a simple algebraic equation."""
        try:
            x = symbols('x')
            eq = Eq(eval(equation.replace("=", "-(") + ")"), 0)
            solution = solve(eq, x)
            await ctx.send(f"The solution to `{equation}` is `{solution}`.")
        except Exception as e:
            await ctx.send("Could not solve the equation.")

    @commands.command(name="area")
    async def calculate_area(self, ctx, shape: str, *args):
        """Calculates the area of basic shapes."""
        if shape.lower() == "circle" and len(args) == 1:
            radius = float(args[0])
            area = 3.14159 * radius**2
            await ctx.send(f"The area of a circle with radius `{radius}` is `{area}`.")
        elif shape.lower() == "square" and len(args) == 1:
            side = float(args[0])
            area = side**2
            await ctx.send(f"The area of a square with side `{side}` is `{area}`.")
        else:
            await ctx.send("Unsupported shape or wrong number of arguments.")

def setup(bot):
    bot.add_cog(MathCog(bot))
