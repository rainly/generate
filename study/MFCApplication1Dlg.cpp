
// MFCApplication1Dlg.cpp : ʵ���ļ�
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


// ����Ӧ�ó��򡰹��ڡ��˵���� CAboutDlg �Ի���

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

	// �Ի�������
	enum { IDD = IDD_ABOUTBOX };

protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV ֧��

	// ʵ��
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


// CMFCApplication1Dlg �Ի���



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


// CMFCApplication1Dlg ��Ϣ�������

BOOL CMFCApplication1Dlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// ��������...���˵�����ӵ�ϵͳ�˵��С�

	// IDM_ABOUTBOX ������ϵͳ���Χ�ڡ�
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

	// ���ô˶Ի����ͼ�ꡣ  ��Ӧ�ó��������ڲ��ǶԻ���ʱ����ܽ��Զ�
	//  ִ�д˲���
	SetIcon(m_hIcon, TRUE);			// ���ô�ͼ��
	SetIcon(m_hIcon, FALSE);		// ����Сͼ��

	// TODO:  �ڴ���Ӷ���ĳ�ʼ������
	m_WebBrower.Navigate(_T("https://www.baidu.com"), NULL, NULL, NULL, NULL);

	//CComVariant vtUrl(L"http://admin:123@172.31.102.12/cgi-bin/va100p.cgi");//ָ����Ҫ�򿪵���ҳ  
	//CComVariant vtEmpty;
	//m_WebBrower.Navigate2(&vtUrl, &vtEmpty, &vtEmpty, &vtEmpty, &vtEmpty);//��ָ����ҳ  
	return TRUE;  // ���ǽ��������õ��ؼ������򷵻� TRUE
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

// �����Ի��������С����ť������Ҫ����Ĵ���
//  �����Ƹ�ͼ�ꡣ  ����ʹ���ĵ�/��ͼģ�͵� MFC Ӧ�ó���
//  �⽫�ɿ���Զ���ɡ�

void CMFCApplication1Dlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // ���ڻ��Ƶ��豸������

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// ʹͼ���ڹ����������о���
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// ����ͼ��
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

//���û��϶���С������ʱϵͳ���ô˺���ȡ�ù��
//��ʾ��
HCURSOR CMFCApplication1Dlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}




void CMFCApplication1Dlg::OnBnClickedOk()
{
	// TODO:  �ڴ���ӿؼ�֪ͨ����������
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
				js_code = L"javascript:document.getElementById('kw').value = '11233'; void(0);";//�˴�Ϊʵ��д���javascript����  
				//js_code.Format(L"goToLocation('%s');",JScode);//JS������+����    
				VARIANT  ret;
				ret.vt = VT_EMPTY;
				pHTMLWnd->execScript(js_code.AllocSysString(), L"Javascript", &ret);//ִ��javascript����  
			}
		}
	}
	{
		CComQIPtr<IHTMLInputElement> spInputElement;
		CComQIPtr<IHTMLDocument3> spDocument = m_WebBrower.get_Document();
		CComPtr<IHTMLElement> spElement;
		spDocument->getElementById(L"kw", &spElement);//ͨ��ID���Ԫ�ض������spElement�У������ID��100���������Ϳ��ԶԸö�����в���  
		if (spElement != NULL)//����ID֮��������ж��¸�ID�Ƿ����  
		{
			//����������ı��򣬿������淽������д��  
			spInputElement = spElement;
			spInputElement->put_value(_T("456"));
			spElement.Release();
		}
		//{
		//	//��������������б����������������ѡ��  
		//	CComVariant vtUrl(L"1-door");
		//	spElement->setAttribute(L"value", vtUrl);
		//	spElement.Release();//������Ҫ���ͷŵ�Ԫ�ض���
		//}
		//{
		//	//��������ǰ�ť���������淽������ģ����  
		//	spElement->click();
		//	spElement.Release();
		//}
		{
		}
		//{
		//	//���������value,�������淽�����  
		//	BSTR BSvalue;
		//	spInputElement = spElement;
		//	spInputElement->get_value(&BSvalue);//�õ�����value�ŵ�BSvalue��
		//	spElement.Release();
		//}

		//*[@id="su"]
		//spDocument->getElementById(L"su", &spElement);//ͨ��ID���Ԫ�ض������spElement�У������ID��100���������Ϳ��ԶԸö�����в���  
		//if (spElement != NULL)//����ID֮��������ж��¸�ID�Ƿ����  
		//{
		//	//��������ǰ�ť���������淽������ģ����  
		//	spElement->click();
		//	spElement.Release();
		//}
		//spDocument->getElementById(L"1", &spElement);//ͨ��ID���Ԫ�ض������spElement�У������ID��100���������Ϳ��ԶԸö�����в���  
		//if (spElement != NULL)//����ID֮��������ж��¸�ID�Ƿ����  
		//{
		//	//��������ǰ�ť���������淽������ģ����  
		//	spElement->click();
		//	spElement.Release();
		//}
		IHTMLElement *loginSubElet = GetHTMLElementByTag(L"input", L"value", L"�ٶ�һ��");
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
	// TODO:  �ڴ˴������Ϣ����������
	//1.�������ȡ�������ҳ������
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
			BSTR html;//���htmlԴ����  
			CComBSTR html_t;//���ڽ�BSTRת��Ϊcout���Դ�����ַ���  
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
	//2.�й������ȡ�������ҳ��cookie
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
			//����  
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
						CComDispatchDriver spInputElement; //ȡ�õ� i ��  
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
						//CComVariant vName,vVal,vType; //����ֵ������  
						//hr = spInputElement.GetPropertyByName( L"name", &vName );  
						//if( FAILED( hr ) ) continue;  
						//hr = spInputElement.GetPropertyByName( L"value", &vVal );  
						//if( FAILED( hr ) ) continue;  
						//hr = spInputElement.GetPropertyByName( L"type", &vType );  
						//if( FAILED( hr ) ) continue;  
						//LPCTSTR lpName = vName.bstrVal?  
						//  OLE2CT( vName.bstrVal ) : _T("NULL"); //δ֪����  
						//LPCTSTR lpVal  = vVal.bstrVal?  
						//  OLE2CT( vVal.bstrVal  ) : _T("NULL"); //��ֵ��δ����  
						//LPCTSTR lpType = vType.bstrVal?  
						//  OLE2CT( vType.bstrVal ) : _T("NULL"); //δ֪����  
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
			//����  
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
