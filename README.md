# Test automation framework for AutoCAD Web
This is a small PoC of a framework that can be used to test [AutoCAD Web](https://web.autocad.com/) application.
It uses Playwright with Pytest and visual comparison.

Refer to article in dev.to for more details: [Test automation for AutoCAD Web using Playwright and visual comparison](https://dev.to/chavus/automating-autocad-web-test-using-playwright-and-visual-comparison-2hll-temp-slug-1216904?preview=48f59d3a284c9efbac101b612319c0c0ba14d724400293cb1e296c068bccc67d8fde51bde329808fe41e0122b55b20900f7f240a4c464996201a3920)

Watch demo video here: [DEMO](https://www.youtube.com/watch?v=LeT0fG1oRAc)

## Project set up
1. Clone repository
2. Create and activate virtual environment
3. Install packages `pip install -r requirements.txt`
4. Configure credentials for AutoCAD Web in `.env` file. A trial account can be used.  
```commandline
APP_USERNAME=ausername
APP_PASSWORD=apassword
```

## Execution
**NOTE:** First execution test will fail, and the reference images for visual comparison will be created under `tests/snapshots` dir
From command line execute:
```commandline
pytest -v --headed --browser-channel chrome --base-url https://web.autocad.com -m regression
```
