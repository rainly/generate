
// MFCApplication1Dlg.h : 头文件
//

#pragma once
#include "explorer1.h"

#include <atlbase.h>
#include "atlconv.h"
#include "Mshtml.h"

#include <string>
using namespace std;


// CMFCApplication1Dlg 对话框
class CMFCApplication1Dlg : public CDialogEx
{
// 构造
public:
	CMFCApplication1Dlg(CWnd* pParent = NULL);	// 标准构造函数

// 对话框数据
	enum { IDD = IDD_MFCAPPLICATION1_DIALOG };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV 支持


// 实现
protected:
	HICON m_hIcon;

	// 生成的消息映射函数
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()
public:
	CExplorer1 m_WebBrower;
	afx_msg void OnBnClickedOk();
	DECLARE_EVENTSINK_MAP()
	void DocumentCompleteExplorer1(LPDISPATCH pDisp, VARIANT* URL);


	IHTMLElement * GetHTMLElementByTag(std::wstring tagName, std::wstring PropertyName,std::wstring macthValue);

	IHTMLElement * GetHTMLElementByIdOrName(std::wstring idorName);
};
