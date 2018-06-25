#include<cstdlib>
#include<iostream> 
#include<vector>
#include<fstream>
#include<string>
#include<ctime>
#include<algorithm>

using namespace std;

void quick_sort(vector<string>& k, vector<string>& v,int start,int end,int count)
{
	if(start>=end)
		return;
	string mid = k[end];
	int left = start,right = end-1;
	while(left<right)
	{
		while(k[left] < mid && left < right)
			left++;
		while(k[right] >= mid && left < right)
			right--;
		swap(k[left],k[right]);
		swap(v[left],v[right]);
	}
	if(k[left] >= k[end])
	{
		swap(k[left],k[end]);
		swap(v[left],v[end]);
	}
	else
		left++;
	quick_sort(k,v,start,left-1,count+1);
	quick_sort(k,v,left+1,end,count+1);
}

int main(int argc,char* argv[])
{
	clock_t time1 = clock();
	char buffer[5000];

	fstream inputfile;
	inputfile.open(argv[1],ios::in);
	fstream outputfile;

	/* Import Python library */
	outputfile.open(argv[2],ios::out);
	outputfile << "import sys" << endl;
	outputfile << "import json" << endl;


	if(!inputfile)
	{cout << "File cannot be open!!" << endl;}
	else
	{
		/* Get the key and value string. */
		int line = 0;
		inputfile.getline(buffer,sizeof(buffer));
		vector<string> allkey;
		vector<string> allvalue;
		vector<string> hashkey;
		while(!inputfile.eof())
		{
			line++;
			if(buffer[0] != '{' && buffer[0] != '}')
			{
				bool quotation = false;
				string tmp = "";
				size_t i = 0;
				for(i=0;i<sizeof(buffer);i++)
				{
					if(buffer[i] == '\"' && !quotation)
					{
						quotation = true;
						continue;
					}
					if(buffer[i] == '\"' and quotation)
						break;
					if(quotation)
						tmp += buffer[i];
				}
				allkey.push_back(tmp);
				tmp = "";
				quotation = false;
				i=i+3;
				for(;i<sizeof(buffer);i++)
				{
					if(buffer[i] == '\"' && !quotation)
					{
						quotation = true;
						continue;
					}
					if(buffer[i] == '\"' and quotation)
						break;
					if(quotation)
						tmp += buffer[i];
				}
				allvalue.push_back(tmp);
			}
			inputfile.getline(buffer,sizeof(buffer));
		}
		inputfile.close();
		quick_sort(allkey,allvalue,0,int(allkey.size()-1),0);

		/* Find longest common substring between key and value start from the head. */
		vector<int> commonindex;
		vector<string> diffstring;
		for(size_t i=0; i<allkey.size();i++)
		{
			size_t N=0;
			if(allkey[i].length() > allvalue[i].length())
				N = allvalue[i].length();
			else
				N = allkey[i].length();
			
			int idx = 0;
			string modify = "";
			bool flag = false;
			for(size_t j=0;j<N;j++)
			{
				if(allkey[i][j] !=allvalue[i][j] && !flag)
				{
					break;
				}
				idx++;
			}
			for(size_t j=idx;j<allvalue[i].length();j++)
			{
				modify += allvalue[i][j];
			}
			commonindex.push_back(idx);
			diffstring.push_back(modify);
		}

		/* Output Python Dictionary */
		outputfile << "d = {";
		for(size_t i=0;i<allkey.size();i++)
		{
			outputfile << i << ":";
			if(diffstring[i].length()==0 && allkey[i].length()==allvalue[i].length())
				outputfile << "\"\"";
			else
				outputfile << "(" << commonindex[i] << ",\"" << diffstring[i] << "\")";
			if(i != allkey.size()-1)
				outputfile << ",";
		}
		outputfile << "}" << endl;
		
	}
	
	/* Output Python: Mapping Procedure. */	
	outputfile << "import time" << endl;
	outputfile << "t1 = time.clock()" << endl;
	outputfile << "f = open(sys.argv[1],'r',encoding = 'UTF-8')" << endl;
	outputfile << "n = json.load(f)[0]" << endl;
	outputfile << "f.close()" << endl;
	outputfile << "n.sort()" << endl;
	outputfile << "f = open(sys.argv[2],'w')" << endl;
	outputfile << "f.write(\"{\\n\")" << endl;
	outputfile << "for i in range(len(n)):" << endl;
	outputfile << "\tif len(d[i])==0:" << endl;
	outputfile << "\t\tf.write('\\\"'+n[i]+'\\\":\\\"'+n[i]+'\\\"')" << endl;
	outputfile << "\telse:" << endl;
	outputfile << "\t\tf.write('\\\"'+n[i]+'\\\":\\\"'+n[i][0:d[i][0]]+d[i][1]+'\\\"')" << endl;
	outputfile << "\tif i!=len(n)-1:" << endl;
	outputfile << "\t\tf.write(\",\")" << endl;
	outputfile << "\tf.write(\"\\n\")" << endl;
	outputfile << "f.write(\"}\")" << endl;
	outputfile << "f.close()" << endl;
	outputfile << "t2 = time.clock()" << endl;
	outputfile << "print(\"Mapping Time usage: \"+str(t2-t1)+\" seconds.\")" << endl;
	outputfile.close();
	
	/* Compare the Input and Output File Size. */
	fstream f1;
	f1.open(argv[1],ios::in);
	f1.seekg(0,ios::end);
	long long length1 = f1.tellg();
	f1.close();
	fstream f2;
	f2.open(argv[2],ios::in);
	f2.seekg(0,ios::end);
	long long length2 = f2.tellg();
	f2.close();
	cout << "  =======================================" << endl;
	cout << "  | Input  Json   File : " << length1 << " bytes." << endl;
	cout << "  | Output Python File : " << length2 << " bytes." << endl;
	cout << "  | New/Old Ratio      : " << 100.0*float(length2)/float(length1) << " %" << endl;
	cout << "  =======================================" << endl;

	/* Time Usage */
	clock_t time2 = clock();
	cout << "Create Python Script Time Usage: " << float(time2-time1)/CLOCKS_PER_SEC << " seconds." << endl;
}
