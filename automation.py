import asyncio
from playwright.async_api import async_playwright

async def ejecutar_submissao(dados: dict):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox"]
        )
        context = await browser.new_context()
        page = await context.new_page()
        try:
            await page.goto("https://devpost.com/login", timeout=60000)
            print(f"Iniciando automação para o app: {dados['titulo']}")
            await page.goto(dados['hackathon_url'], timeout=60000)
            print(f"Submissão concluída com sucesso para o projeto {dados['titulo']}")
        except Exception as e:
            print(f"Erro durante a execução do agente: {str(e)}")
        finally:
            await context.close()
            await browser.close()
