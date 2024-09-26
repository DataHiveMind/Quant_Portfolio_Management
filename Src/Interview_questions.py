def max_drawdown(pnls):
    """
    Calculate the maximum drawdown of a list of daily portfolio PnLs.

    Parameters:
    pnls (list of float): List of daily portfolio PnLs.

    Returns:
    float: The maximum drawdown.
    """
    max_drawdown = 0
    peak = pnls[0]
    
    for pnl in pnls:
        if pnl > peak:
            peak = pnl
        drawdown = (peak - pnl) / peak
        if drawdown > max_drawdown:
            max_drawdown = drawdown
    
    return max_drawdown



