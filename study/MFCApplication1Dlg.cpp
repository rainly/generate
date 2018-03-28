
// MFCApplication1Dlg.cpp : 实现文件
//

#include "stdafx.h"
#include "MFCApplication1.h"
#include "MFCApplication1Dlg.h"
#include "afxdialogex.h"
#include <atlbase.h>
#include "atlconv.h"
#include "Mshtml.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// 用于应用程序“关于”菜单项的 CAboutDlg 对话框

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

	// 对话框数据
	enum { IDD = IDD_ABOUTBOX };

protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV 支持

	// 实现
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialogEx(CAboutDlg::IDD)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CMFCApplication1Dlg 对话框



CMFCApplication1Dlg::CMFCApplication1Dlg(CWnd* pParent /*=NULL*/)
	: CDialogEx(CMFCApplication1Dlg::IDD, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CMFCApplication1Dlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
	DDX_Control(pDX, IDC_EXPLORER1, m_WebBrower);
}

BEGIN_MESSAGE_MAP(CMFCApplication1Dlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDOK, &CMFCApplication1Dlg::OnBnClickedOk)
END_MESSAGE_MAP()


// CMFCApplication1Dlg 消息处理程序

BOOL CMFCApplication1Dlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// 将“关于...”菜单项添加到系统菜单中。

	// IDM_ABOUTBOX 必须在系统命令范围内。
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// 设置此对话框的图标。  当应用程序主窗口不是对话框时，框架将自动
	//  执行此操作
	SetIcon(m_hIcon, TRUE);			// 设置大图标
	SetIcon(m_hIcon, FALSE);		// 设置小图标

	// TODO:  在此添加额外的初始化代码
	m_WebBrower.Navigate(_T("https://www.baidu.com"), NULL, NULL, NULL, NULL);

	//CComVariant vtUrl(L"http://admin:123@172.31.102.12/cgi-bin/va100p.cgi");//指定需要打开的网页  
	//CComVariant vtEmpty;
	//m_WebBrower.Navigate2(&vtUrl, &vtEmpty, &vtEmpty, &vtEmpty, &vtEmpty);//打开指定网页  
	return TRUE;  // 除非将焦点设置到控件，否则返回 TRUE
}

void CMFCApplication1Dlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialogEx::OnSysCommand(nID, lParam);
	}
}

// 如果向对话框添加最小化按钮，则需要下面的代码
//  来绘制该图标。  对于使用文档/视图模型的 MFC 应用程序，
//  这将由框架自动完成。

void CMFCApplication1Dlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // 用于绘制的设备上下文

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// 使图标在工作区矩形中居中
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// 绘制图标
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

//当用户拖动最小化窗口时系统调用此函数取得光标
//显示。
HCURSOR CMFCApplication1Dlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}




void CMFCApplication1Dlg::OnBnClickedOk()
{
	// TODO:  在此添加控件通知处理程序代码
	//CDialogEx::OnOK();
	{
		IHTMLDocument2* pHTMLDoc = (IHTMLDocument2*)m_WebBrower.get_Document();
		if (pHTMLDoc != NULL)
		{
			IHTMLWindow2* pHTMLWnd;
			pHTMLDoc->get_parentWindow(&pHTMLWnd);
			if (pHTMLWnd != NULL)
			{
				CString js_code;
				js_code = L"javascript:document.getElementById('kw').value = '11233'; void(0);";//此次为实际写入的javascript代码  
				//js_code.Format(L"goToLocation('%s');",JScode);//JS函数名+参数    
				VARIANT  ret;
				ret.vt = VT_EMPTY;
				pHTMLWnd->execScript(js_code.AllocSysString(), L"Javascript", &ret);//执行javascript代码  
			}
		}
	}
	{
		CComQIPtr<IHTMLInputElement> spInputElement;
		CComQIPtr<IHTMLDocument3> spDocument = m_WebBrower.get_Document();
		CComPtr<IHTMLElement> spElement;
		spDocument->getElementById(L"kw", &spElement);//通过ID获得元素对象存在spElement中，这里的ID是100，接下来就可以对该对象进行操作  
		if (spElement != NULL)//读入ID之后可以先判断下该ID是否存在  
		{
			//如果对象是文本框，可用下面方法进行写入  
			spInputElement = spElement;
			spInputElement->put_value(_T("456"));
			spElement.Release();
		}
		//{
		//	//如果对象是下拉列表框，则经由下面代码进行选择  
		//	CComVariant vtUrl(L"1-door");
		//	spElement->setAttribute(L"value", vtUrl);
		//	spElement.Release();//操作后要设释放掉元素对象
		//}
		//{
		//	//如果对象是按钮，可用下面方法进行模拟点击  
		//	spElement->click();
		//	spElement.Release();
		//}
		{
		}
		//{
		//	//如果对象有value,可用下面方法获得  
		//	BSTR BSvalue;
		//	spInputElement = spElement;
		//	spInputElement->get_value(&BSvalue);//得到对象value放到BSvalue中
		//	spElement.Release();
		//}

		//*[@id="su"]
		//spDocument->getElementById(L"su", &spElement);//通过ID获得元素对象存在spElement中，这里的ID是100，接下来就可以对该对象进行操作  
		//if (spElement != NULL)//读入ID之后可以先判断下该ID是否存在  
		//{
		//	//如果对象是按钮，可用下面方法进行模拟点击  
		//	spElement->click();
		//	spElement.Release();
		//}
		//spDocument->getElementById(L"1", &spElement);//通过ID获得元素对象存在spElement中，这里的ID是100，接下来就可以对该对象进行操作  
		//if (spElement != NULL)//读入ID之后可以先判断下该ID是否存在  
		//{
		//	//如果对象是按钮，可用下面方法进行模拟点击  
		//	spElement->click();
		//	spElement.Release();
		//}
		IHTMLElement *loginSubElet = GetHTMLElementByTag(L"input", L"value", L"百度一下");
		if (loginSubElet != NULL)
		{
			loginSubElet->click();
			loginSubElet->Release();
		}

	}
}
////*[@id="kw"]
BEGIN_EVENTSINK_MAP(CMFCApplication1Dlg, CDialogEx)
	ON_EVENT(CMFCApplication1Dlg, IDC_EXPLORER1, 259, CMFCApplication1Dlg::DocumentCompleteExplorer1, VTS_DISPATCH VTS_PVARIANT)
END_EVENTSINK_MAP()


void CMFCApplication1Dlg::DocumentCompleteExplorer1(LPDISPATCH pDisp, VARIANT* URL)
{
	// TODO:  在此处添加消息处理程序代码
	//1.关于如何取得这个网页的内容
	{
		HRESULT hr;
		IDispatch* lpDispatch;
		lpDispatch = m_WebBrower.get_Document();
		IHTMLDocument2* lpDocument2;
		hr = lpDispatch->QueryInterface(IID_IHTMLDocument2, (PVOID*)&lpDocument2);
		if (hr == S_OK)
		{
			IHTMLElement * pBody;
			lpDocument2->get_body(&pBody);
			BSTR html;//存放html源代码  
			CComBSTR html_t;//用于将BSTR转换为cout可以处理的字符串  
			pBody->get_innerHTML(&html);
			CString strCookie(html);
			CFile myfile(_T("1.html"), CFile::modeWrite | CFile::modeCreate);
			myfile.Write(strCookie, strCookie.GetLength());
			myfile.Close();
			pBody->Release();
			lpDocument2->Release();
		}
		lpDispatch->Release();
	}
	//2.有关于如何取得这个网页的cookie
	{
		HRESULT hr;
		IDispatch* lpDispatch;
		lpDispatch = m_WebBrower.get_Document();
		IHTMLDocument2* lpDocument2;
		hr = lpDispatch->QueryInterface(IID_IHTMLDocument2, (PVOID*)&lpDocument2);
		if (hr == S_OK)
		{
			BSTR bstrCookie;
			hr = lpDocument2->get_cookie(&bstrCookie);
			if (hr == S_OK)
			{
				CString strCookie(bstrCookie);
				CFile myfile(_T("1.txt"), CFile::modeWrite | CFile::modeCreate);
				myfile.Write(strCookie, strCookie.GetLength());
				myfile.Close();
			}
			lpDocument2->put_cookie(NULL);
			//pBody->Release();
			lpDocument2->Release();
		}
		lpDispatch->Release();
	}
}

IHTMLElement * CMFCApplication1Dlg::GetHTMLElementByTag(std::wstring tagName, std::wstring PropertyName,
	std::wstring macthValue)
{
	HRESULT hr;
	IHTMLElement *retElement = 0;
	IDispatch *lpDispatch = 0;
	lpDispatch = m_WebBrower.get_Document();
	IHTMLDocument2* lpDocument2;
	hr = lpDispatch->QueryInterface(IID_IHTMLDocument2, (PVOID*)&lpDocument2);
	if (hr == S_OK)
	{
		lpDispatch->Release();
		IHTMLElementCollection* doc_all;
		hr = lpDocument2->get_all(&doc_all);      // this is like doing document.all  
		if (S_OK == hr)
		{
			VARIANT vKey;
			vKey.vt = VT_BSTR;
			vKey.bstrVal = SysAllocString(tagName.c_str());
			VARIANT vIndex;
			VariantInit(&vIndex);
			hr = doc_all->tags(vKey, &lpDispatch);       // this is like doing document.all["messages"]  
			//清理  
			SysFreeString(vKey.bstrVal);
			VariantClear(&vKey);
			VariantClear(&vIndex);
			if ((S_OK == hr) && (0 != lpDispatch))
			{
				CComQIPtr< IHTMLElementCollection > all_tags = lpDispatch;
				//hr = dispatch->QueryInterface(IHTMLElementCollection,(void **)&all_tags); // it's the caller's responsibility to release   
				if (S_OK == hr)
				{
					long nTagsCount = 0; //  
					hr = all_tags->get_length(&nTagsCount);
					if (FAILED(hr))
					{
						return retElement;
					}

					for (long i = 0; i < nTagsCount; i++)
					{
						CComDispatchDriver spInputElement; //取得第 i 项  
						hr = all_tags->item(CComVariant(i), CComVariant(i), &spInputElement);

						if (FAILED(hr))
							continue;
						CComVariant vValue;
						hr = spInputElement.GetPropertyByName(PropertyName.c_str(), &vValue);
						if (VT_EMPTY != vValue.vt)
						{
							LPCTSTR lpValue = vValue.bstrVal ?
								OLE2CT(vValue.bstrVal) : NULL;
							if (NULL == lpValue)
								continue;
							std::wstring cs = (LPCTSTR)lpValue;
							if (0 == _tcscmp(cs.c_str(), macthValue.c_str()))
							{
								hr = spInputElement->QueryInterface(IID_IHTMLElement, (void **)&retElement);
								if (S_OK == hr)
								{
								}
								else
								{
									retElement = 0;
								}
								break;
							}
						}
						//  
						//CComVariant vName,vVal,vType; //名，值，类型  
						//hr = spInputElement.GetPropertyByName( L"name", &vName );  
						//if( FAILED( hr ) ) continue;  
						//hr = spInputElement.GetPropertyByName( L"value", &vVal );  
						//if( FAILED( hr ) ) continue;  
						//hr = spInputElement.GetPropertyByName( L"type", &vType );  
						//if( FAILED( hr ) ) continue;  
						//LPCTSTR lpName = vName.bstrVal?  
						//  OLE2CT( vName.bstrVal ) : _T("NULL"); //未知域名  
						//LPCTSTR lpVal  = vVal.bstrVal?  
						//  OLE2CT( vVal.bstrVal  ) : _T("NULL"); //空值，未输入  
						//LPCTSTR lpType = vType.bstrVal?  
						//  OLE2CT( vType.bstrVal ) : _T("NULL"); //未知类型  
					}
				}
				else
				{
					retElement = 0;
				}
				lpDispatch->Release();
			}
			doc_all->Release();
		}
		lpDocument2->Release();
	}
	return retElement;
}

IHTMLElement * CMFCApplication1Dlg::GetHTMLElementByIdOrName(std::wstring idorName)
{
	IHTMLElement *retElement = 0;
	IDispatch *dispatch = 0;
	HRESULT hr;
	dispatch = m_WebBrower.get_Document();
	if (0 != dispatch)
	{
		IHTMLDocument2 *doc;
		dispatch->QueryInterface(IID_IHTMLDocument2, (void**)&doc);
		dispatch->Release();
		IHTMLElementCollection* doc_all;
		hr = doc->get_all(&doc_all);      // this is like doing document.all  
		if (S_OK == hr)
		{
			VARIANT vKey;
			vKey.vt = VT_BSTR;
			vKey.bstrVal = SysAllocString(idorName.c_str());
			VARIANT vIndex;
			VariantInit(&vIndex);
			hr = doc_all->item(vKey, vIndex, &dispatch);       // this is like doing document.all["messages"]  
			//清理  
			SysFreeString(vKey.bstrVal);
			VariantClear(&vKey);
			VariantClear(&vIndex);
			if ((S_OK == hr) && (0 != dispatch))
			{
				hr = dispatch->QueryInterface(IID_IHTMLElement, (void **)&retElement); // it's the caller's responsibility to release   
				if (S_OK == hr)
				{
				}
				else
				{
					retElement = 0;
				}
				dispatch->Release();
			}
			doc_all->Release();
		}
		doc->Release();
	}
	return retElement;
}
