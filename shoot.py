import asyncio, json, pathlib
from playwright.async_api import async_playwright
root=pathlib.Path(__file__).parent
sizes=[("320-mobile",320,640),("768-tablet",768,1024),("1024-laptop",1024,768),("1440-desktop",1440,900)]
async def main():
    res=[]
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for theme in ("light","dark"):
            for name,w,h in sizes:
                pg=await b.new_page(viewport={"width":w,"height":h},color_scheme=theme)
                await pg.goto((root/"index.html").as_uri()); await pg.wait_for_timeout(300)
                sw=await pg.evaluate("[document.documentElement.scrollWidth,document.documentElement.clientWidth]")
                res.append(f"{name:14} {theme:5} scrollWidth={sw[0]} clientWidth={sw[1]} -> {'OK' if sw[0]<=sw[1] else 'OVERFLOW'}")
                await pg.screenshot(path=str(root/"screenshots"/f"{name}-{theme}.png"),full_page=True)
                await pg.close()
        await b.close()
    print("\n".join(res))
asyncio.run(main())
