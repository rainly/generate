
// MFCApplication1Dlg.h : ͷ�ļ�
//

#pragma once
#include "explorer1.h"

#include <atlbase.h>
#include "atlconv.h"
#include "Mshtml.h"

#include <string>
using namespace std;


// CMFCApplication1Dlg �Ի���
class CMFCApplication1Dlg : public CDialogEx
{
// ����
public:
	CMFCApplication1Dlg(CWnd* pParent = NULL);	// ��׼���캯��

// �Ի�������
	enum { IDD = IDD_MFCAPPLICATION1_DIALOG };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV ֧��


// ʵ��
protected:
	HICON m_hIcon;

	// ���ɵ���Ϣӳ�亯��
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
