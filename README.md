# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.84</td>
    <td align="right">4.50</td>
    <td align="right">3.69</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">11.22</td>
    <td align="right">10.01</td>
    <td align="right">15.85</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.05</td>
    <td align="right">4.43</td>
    <td align="right">4.42</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.86</td>
    <td align="right">5.08</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.45</td>
    <td align="right">15.53</td>
    <td align="right">17.55</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.80</td>
    <td align="right">4.93</td>
    <td align="right">4.96</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.41</td>
    <td align="right">5.50</td>
    <td align="right">5.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.64</td>
    <td align="right">18.83</td>
    <td align="right">16.48</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.37</td>
    <td align="right">5.32</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.24</td>
    <td align="right">6.29</td>
    <td align="right">6.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.50</td>
    <td align="right">22.72</td>
    <td align="right">16.74</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.40</td>
    <td align="right">6.09</td>
    <td align="right">5.90</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.66</td>
    <td align="right">6.59</td>
    <td align="right">6.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1818</td>
    <td align="right">10.62</td>
    <td align="right">10.99</td>
    <td align="right">16.94</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">3.84</td>
    <td align="right">4.40</td>
    <td align="right">4.42</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">4.60</td>
    <td align="right">5.23</td>
    <td align="right">5.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">15.84</td>
    <td align="right">15.97</td>
    <td align="right">17.92</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">4.40</td>
    <td align="right">5.26</td>
    <td align="right">5.27</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">5.32</td>
    <td align="right">5.82</td>
    <td align="right">5.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">18.32</td>
    <td align="right">19.14</td>
    <td align="right">17.16</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">4.97</td>
    <td align="right">5.66</td>
    <td align="right">5.62</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">5.67</td>
    <td align="right">6.48</td>
    <td align="right">6.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">23.49</td>
    <td align="right">24.30</td>
    <td align="right">17.08</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">5.33</td>
    <td align="right">6.26</td>
    <td align="right">6.27</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">6.16</td>
    <td align="right">6.79</td>
    <td align="right">6.80</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.05</td>
    <td align="right">5.73</td>
    <td align="right">5.73</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.48</td>
    <td align="right">6.63</td>
    <td align="right">6.80</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.92</td>
    <td align="right">3.25</td>
    <td align="right">3.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.97</td>
    <td align="right">8.83</td>
    <td align="right">8.80</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.13</td>
    <td align="right">9.97</td>
    <td align="right">9.97</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.46</td>
    <td align="right">3.10</td>
    <td align="right">3.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.18</td>
    <td align="right">13.70</td>
    <td align="right">13.86</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.60</td>
    <td align="right">13.94</td>
    <td align="right">13.93</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.66</td>
    <td align="right">5.67</td>
    <td align="right">3.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">10.96</td>
    <td align="right">15.39</td>
    <td align="right">15.37</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">11.87</td>
    <td align="right">17.41</td>
    <td align="right">17.33</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.72</td>
    <td align="right">5.73</td>
    <td align="right">3.82</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">4.79</td>
    <td align="right">5.89</td>
    <td align="right">5.89</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">5.65</td>
    <td align="right">6.74</td>
    <td align="right">6.74</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">3.03</td>
    <td align="right">2.90</td>
    <td align="right">2.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">6.15</td>
    <td align="right">8.99</td>
    <td align="right">9.00</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">7.34</td>
    <td align="right">9.94</td>
    <td align="right">9.94</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.52</td>
    <td align="right">2.80</td>
    <td align="right">2.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">9.04</td>
    <td align="right">12.99</td>
    <td align="right">12.97</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">16.82</td>
    <td align="right">14.66</td>
    <td align="right">14.65</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">5.70</td>
    <td align="right">5.94</td>
    <td align="right">3.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">11.10</td>
    <td align="right">14.93</td>
    <td align="right">14.92</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">12.04</td>
    <td align="right">17.41</td>
    <td align="right">17.44</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">5.70</td>
    <td align="right">5.99</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.91</td>
    <td align="right">3.18</td>
    <td align="right">3.18</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.38</td>
    <td align="right">5.03</td>
    <td align="right">4.97</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.50</td>
    <td align="right">4.92</td>
    <td align="right">5.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.01</td>
    <td align="right">3.28</td>
    <td align="right">3.26</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.17</td>
    <td align="right">4.42</td>
    <td align="right">4.42</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.42</td>
    <td align="right">5.06</td>
    <td align="right">5.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.37</td>
    <td align="right">5.42</td>
    <td align="right">3.69</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">6.93</td>
    <td align="right">7.62</td>
    <td align="right">5.82</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.83</td>
    <td align="right">7.74</td>
    <td align="right">5.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.44</td>
    <td align="right">5.52</td>
    <td align="right">3.74</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">7.98</td>
    <td align="right">9.02</td>
    <td align="right">5.96</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.27</td>
    <td align="right">8.91</td>
    <td align="right">5.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4739</td>
    <td align="right">3.09</td>
    <td align="right">2.76</td>
    <td align="right">2.76</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">4.55</td>
    <td align="right">4.73</td>
    <td align="right">4.76</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">4.54</td>
    <td align="right">4.63</td>
    <td align="right">4.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.19</td>
    <td align="right">2.84</td>
    <td align="right">2.83</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">3.26</td>
    <td align="right">4.01</td>
    <td align="right">3.99</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">4.53</td>
    <td align="right">4.74</td>
    <td align="right">4.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">5.30</td>
    <td align="right">5.62</td>
    <td align="right">3.76</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">7.30</td>
    <td align="right">7.78</td>
    <td align="right">5.94</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">7.76</td>
    <td align="right">7.53</td>
    <td align="right">5.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">5.35</td>
    <td align="right">5.85</td>
    <td align="right">3.76</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">7.94</td>
    <td align="right">9.13</td>
    <td align="right">5.95</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">8.24</td>
    <td align="right">8.86</td>
    <td align="right">5.77</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.57</td>
    <td align="right">17.95</td>
    <td align="right">6.76</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.06</td>
    <td align="right">12.77</td>
    <td align="right">17.61</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.77</td>
    <td align="right">5.14</td>
    <td align="right">5.10</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.72</td>
    <td align="right">5.92</td>
    <td align="right">5.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.78</td>
    <td align="right">18.40</td>
    <td align="right">18.20</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.45</td>
    <td align="right">5.60</td>
    <td align="right">5.61</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.16</td>
    <td align="right">6.22</td>
    <td align="right">6.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">26.53</td>
    <td align="right">24.55</td>
    <td align="right">17.63</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.60</td>
    <td align="right">6.53</td>
    <td align="right">6.63</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.85</td>
    <td align="right">7.98</td>
    <td align="right">7.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">45.19</td>
    <td align="right">42.87</td>
    <td align="right">19.10</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">10.45</td>
    <td align="right">10.28</td>
    <td align="right">10.10</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">10.50</td>
    <td align="right">10.22</td>
    <td align="right">10.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1556</td>
    <td align="right">13.12</td>
    <td align="right">13.45</td>
    <td align="right">18.11</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">4.55</td>
    <td align="right">5.12</td>
    <td align="right">5.15</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">5.53</td>
    <td align="right">6.14</td>
    <td align="right">6.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">18.85</td>
    <td align="right">19.10</td>
    <td align="right">17.49</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">5.07</td>
    <td align="right">5.90</td>
    <td align="right">5.93</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">6.04</td>
    <td align="right">6.53</td>
    <td align="right">6.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">24.96</td>
    <td align="right">23.87</td>
    <td align="right">17.86</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">6.54</td>
    <td align="right">7.08</td>
    <td align="right">7.14</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">7.13</td>
    <td align="right">7.91</td>
    <td align="right">7.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">43.59</td>
    <td align="right">44.93</td>
    <td align="right">19.72</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">9.38</td>
    <td align="right">10.55</td>
    <td align="right">10.26</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">9.51</td>
    <td align="right">10.24</td>
    <td align="right">10.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.06</td>
    <td align="right">6.94</td>
    <td align="right">6.92</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.64</td>
    <td align="right">8.01</td>
    <td align="right">8.29</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.57</td>
    <td align="right">4.08</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.03</td>
    <td align="right">9.78</td>
    <td align="right">9.82</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.11</td>
    <td align="right">11.08</td>
    <td align="right">11.10</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.01</td>
    <td align="right">3.90</td>
    <td align="right">3.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.31</td>
    <td align="right">15.40</td>
    <td align="right">15.53</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.85</td>
    <td align="right">15.88</td>
    <td align="right">15.92</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.25</td>
    <td align="right">7.44</td>
    <td align="right">5.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.56</td>
    <td align="right">19.79</td>
    <td align="right">20.06</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.56</td>
    <td align="right">22.26</td>
    <td align="right">22.10</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.12</td>
    <td align="right">10.01</td>
    <td align="right">7.02</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">5.72</td>
    <td align="right">7.10</td>
    <td align="right">7.13</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">6.88</td>
    <td align="right">8.14</td>
    <td align="right">8.16</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.68</td>
    <td align="right">3.58</td>
    <td align="right">3.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">6.96</td>
    <td align="right">9.94</td>
    <td align="right">9.94</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">8.46</td>
    <td align="right">11.20</td>
    <td align="right">11.17</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">2.95</td>
    <td align="right">3.18</td>
    <td align="right">3.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">11.38</td>
    <td align="right">14.92</td>
    <td align="right">14.94</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">17.88</td>
    <td align="right">17.00</td>
    <td align="right">17.12</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">7.50</td>
    <td align="right">7.79</td>
    <td align="right">5.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">16.42</td>
    <td align="right">18.75</td>
    <td align="right">19.05</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">16.85</td>
    <td align="right">21.93</td>
    <td align="right">21.94</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">10.36</td>
    <td align="right">10.19</td>
    <td align="right">7.46</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.55</td>
    <td align="right">4.01</td>
    <td align="right">3.99</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.21</td>
    <td align="right">6.11</td>
    <td align="right">6.04</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.41</td>
    <td align="right">5.98</td>
    <td align="right">6.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.50</td>
    <td align="right">3.95</td>
    <td align="right">3.94</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.69</td>
    <td align="right">5.10</td>
    <td align="right">5.09</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.99</td>
    <td align="right">5.91</td>
    <td align="right">5.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.92</td>
    <td align="right">7.44</td>
    <td align="right">5.14</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">9.30</td>
    <td align="right">10.55</td>
    <td align="right">8.00</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.43</td>
    <td align="right">9.55</td>
    <td align="right">7.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.46</td>
    <td align="right">10.18</td>
    <td align="right">7.18</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">11.97</td>
    <td align="right">14.23</td>
    <td align="right">9.19</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.94</td>
    <td align="right">14.53</td>
    <td align="right">10.25</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">3.69</td>
    <td align="right">3.44</td>
    <td align="right">3.44</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">5.32</td>
    <td align="right">5.60</td>
    <td align="right">5.61</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">5.40</td>
    <td align="right">5.56</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.70</td>
    <td align="right">3.46</td>
    <td align="right">3.47</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">3.82</td>
    <td align="right">4.63</td>
    <td align="right">4.58</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">5.21</td>
    <td align="right">5.65</td>
    <td align="right">5.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">6.60</td>
    <td align="right">7.25</td>
    <td align="right">4.96</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">9.73</td>
    <td align="right">10.46</td>
    <td align="right">7.97</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">9.48</td>
    <td align="right">9.74</td>
    <td align="right">7.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">8.98</td>
    <td align="right">10.06</td>
    <td align="right">7.07</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">11.42</td>
    <td align="right">14.24</td>
    <td align="right">9.63</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">12.02</td>
    <td align="right">13.95</td>
    <td align="right">9.61</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.84</td>
    <td align="right">4.16</td>
    <td align="right">3.33</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.21</td>
    <td align="right">8.94</td>
    <td align="right">15.44</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.37</td>
    <td align="right">4.04</td>
    <td align="right">3.96</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.88</td>
    <td align="right">4.58</td>
    <td align="right">4.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.18</td>
    <td align="right">14.23</td>
    <td align="right">16.91</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.93</td>
    <td align="right">4.63</td>
    <td align="right">4.58</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.48</td>
    <td align="right">5.30</td>
    <td align="right">5.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.44</td>
    <td align="right">16.84</td>
    <td align="right">15.70</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.40</td>
    <td align="right">5.12</td>
    <td align="right">5.14</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.95</td>
    <td align="right">6.08</td>
    <td align="right">6.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.89</td>
    <td align="right">20.64</td>
    <td align="right">16.32</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.86</td>
    <td align="right">5.90</td>
    <td align="right">5.89</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.90</td>
    <td align="right">3.34</td>
    <td align="right">3.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1818</td>
    <td align="right">10.34</td>
    <td align="right">10.04</td>
    <td align="right">16.42</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">4.28</td>
    <td align="right">4.27</td>
    <td align="right">4.14</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">4.06</td>
    <td align="right">4.93</td>
    <td align="right">4.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">15.60</td>
    <td align="right">15.36</td>
    <td align="right">17.59</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">4.46</td>
    <td align="right">4.57</td>
    <td align="right">4.51</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">4.70</td>
    <td align="right">5.69</td>
    <td align="right">5.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">18.95</td>
    <td align="right">18.43</td>
    <td align="right">16.64</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">5.18</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">5.27</td>
    <td align="right">6.16</td>
    <td align="right">6.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">24.00</td>
    <td align="right">22.98</td>
    <td align="right">16.85</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">5.66</td>
    <td align="right">6.17</td>
    <td align="right">5.97</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">3.23</td>
    <td align="right">3.54</td>
    <td align="right">3.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.09</td>
    <td align="right">3.63</td>
    <td align="right">3.61</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.18</td>
    <td align="right">3.53</td>
    <td align="right">3.52</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.66</td>
    <td align="right">2.52</td>
    <td align="right">2.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.74</td>
    <td align="right">3.41</td>
    <td align="right">3.43</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.77</td>
    <td align="right">3.74</td>
    <td align="right">3.76</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.16</td>
    <td align="right">2.27</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.71</td>
    <td align="right">6.23</td>
    <td align="right">6.22</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.81</td>
    <td align="right">6.14</td>
    <td align="right">6.12</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.23</td>
    <td align="right">4.42</td>
    <td align="right">3.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.04</td>
    <td align="right">6.75</td>
    <td align="right">6.64</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.33</td>
    <td align="right">7.05</td>
    <td align="right">7.27</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.30</td>
    <td align="right">4.44</td>
    <td align="right">3.16</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.24</td>
    <td align="right">3.84</td>
    <td align="right">3.84</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">3.36</td>
    <td align="right">3.74</td>
    <td align="right">3.77</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">2.91</td>
    <td align="right">2.80</td>
    <td align="right">2.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">3.42</td>
    <td align="right">3.73</td>
    <td align="right">3.74</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">3.95</td>
    <td align="right">4.03</td>
    <td align="right">4.05</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.85</td>
    <td align="right">2.64</td>
    <td align="right">2.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">5.87</td>
    <td align="right">6.59</td>
    <td align="right">6.58</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">5.93</td>
    <td align="right">6.72</td>
    <td align="right">6.74</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">4.54</td>
    <td align="right">4.78</td>
    <td align="right">3.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">6.31</td>
    <td align="right">6.81</td>
    <td align="right">7.01</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">6.75</td>
    <td align="right">7.24</td>
    <td align="right">7.25</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">4.54</td>
    <td align="right">4.78</td>
    <td align="right">3.47</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.60</td>
    <td align="right">2.38</td>
    <td align="right">2.35</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.66</td>
    <td align="right">4.07</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.69</td>
    <td align="right">3.99</td>
    <td align="right">3.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.70</td>
    <td align="right">2.45</td>
    <td align="right">2.42</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.97</td>
    <td align="right">3.77</td>
    <td align="right">3.79</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.89</td>
    <td align="right">4.05</td>
    <td align="right">4.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.24</td>
    <td align="right">4.29</td>
    <td align="right">2.95</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.70</td>
    <td align="right">6.03</td>
    <td align="right">4.66</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.87</td>
    <td align="right">6.04</td>
    <td align="right">4.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.31</td>
    <td align="right">4.37</td>
    <td align="right">2.96</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.64</td>
    <td align="right">7.17</td>
    <td align="right">4.91</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.80</td>
    <td align="right">7.10</td>
    <td align="right">4.95</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4739</td>
    <td align="right">2.82</td>
    <td align="right">2.69</td>
    <td align="right">2.69</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">3.87</td>
    <td align="right">4.38</td>
    <td align="right">4.39</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">3.93</td>
    <td align="right">4.33</td>
    <td align="right">4.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.00</td>
    <td align="right">2.77</td>
    <td align="right">2.75</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">3.66</td>
    <td align="right">4.09</td>
    <td align="right">4.07</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">4.19</td>
    <td align="right">4.40</td>
    <td align="right">4.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">4.51</td>
    <td align="right">4.69</td>
    <td align="right">3.25</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">5.93</td>
    <td align="right">6.51</td>
    <td align="right">5.11</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">6.06</td>
    <td align="right">6.42</td>
    <td align="right">4.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">4.50</td>
    <td align="right">4.72</td>
    <td align="right">3.21</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">7.14</td>
    <td align="right">7.59</td>
    <td align="right">5.48</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">7.08</td>
    <td align="right">7.39</td>
    <td align="right">5.25</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">33.69</td>
    <td align="right">16.86</td>
    <td align="right">7.48</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.42</td>
    <td align="right">11.25</td>
    <td align="right">16.62</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.05</td>
    <td align="right">4.64</td>
    <td align="right">4.68</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.66</td>
    <td align="right">5.53</td>
    <td align="right">5.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">18.03</td>
    <td align="right">19.76</td>
    <td align="right">18.41</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.57</td>
    <td align="right">6.42</td>
    <td align="right">7.60</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.09</td>
    <td align="right">7.92</td>
    <td align="right">7.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">39.94</td>
    <td align="right">27.70</td>
    <td align="right">18.04</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">7.82</td>
    <td align="right">9.50</td>
    <td align="right">11.31</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">8.30</td>
    <td align="right">7.69</td>
    <td align="right">8.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">54.78</td>
    <td align="right">64.76</td>
    <td align="right">23.35</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">13.51</td>
    <td align="right">14.83</td>
    <td align="right">19.44</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.05</td>
    <td align="right">9.35</td>
    <td align="right">6.91</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1556</td>
    <td align="right">12.31</td>
    <td align="right">12.55</td>
    <td align="right">17.73</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">5.09</td>
    <td align="right">4.91</td>
    <td align="right">4.85</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">4.85</td>
    <td align="right">5.71</td>
    <td align="right">5.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">18.80</td>
    <td align="right">19.53</td>
    <td align="right">18.60</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">4.89</td>
    <td align="right">4.74</td>
    <td align="right">4.85</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">5.62</td>
    <td align="right">6.25</td>
    <td align="right">6.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">33.14</td>
    <td align="right">31.93</td>
    <td align="right">17.95</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">8.74</td>
    <td align="right">10.04</td>
    <td align="right">8.92</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">8.75</td>
    <td align="right">9.50</td>
    <td align="right">10.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">65.68</td>
    <td align="right">56.98</td>
    <td align="right">21.83</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">8.76</td>
    <td align="right">9.86</td>
    <td align="right">9.08</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">5.48</td>
    <td align="right">7.20</td>
    <td align="right">5.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.62</td>
    <td align="right">4.18</td>
    <td align="right">4.17</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.74</td>
    <td align="right">4.20</td>
    <td align="right">4.17</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.06</td>
    <td align="right">3.04</td>
    <td align="right">3.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.26</td>
    <td align="right">4.16</td>
    <td align="right">4.39</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.17</td>
    <td align="right">4.31</td>
    <td align="right">4.65</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.73</td>
    <td align="right">2.81</td>
    <td align="right">2.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">8.76</td>
    <td align="right">8.84</td>
    <td align="right">10.75</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.97</td>
    <td align="right">7.91</td>
    <td align="right">8.38</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.26</td>
    <td align="right">5.49</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">8.38</td>
    <td align="right">11.84</td>
    <td align="right">9.74</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">11.62</td>
    <td align="right">11.97</td>
    <td align="right">11.82</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">8.10</td>
    <td align="right">10.70</td>
    <td align="right">5.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">3.60</td>
    <td align="right">4.18</td>
    <td align="right">4.18</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">3.97</td>
    <td align="right">4.49</td>
    <td align="right">4.54</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.53</td>
    <td align="right">3.50</td>
    <td align="right">3.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">4.28</td>
    <td align="right">4.41</td>
    <td align="right">4.38</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">4.51</td>
    <td align="right">6.07</td>
    <td align="right">5.29</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">4.78</td>
    <td align="right">4.52</td>
    <td align="right">3.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">9.12</td>
    <td align="right">10.45</td>
    <td align="right">10.78</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">9.88</td>
    <td align="right">10.52</td>
    <td align="right">8.97</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">8.45</td>
    <td align="right">9.96</td>
    <td align="right">6.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">13.00</td>
    <td align="right">15.20</td>
    <td align="right">16.85</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">12.59</td>
    <td align="right">10.97</td>
    <td align="right">10.73</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">8.99</td>
    <td align="right">11.17</td>
    <td align="right">7.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.14</td>
    <td align="right">2.98</td>
    <td align="right">3.01</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.33</td>
    <td align="right">4.94</td>
    <td align="right">4.91</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.48</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.18</td>
    <td align="right">3.10</td>
    <td align="right">3.28</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">4.21</td>
    <td align="right">5.12</td>
    <td align="right">7.21</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.55</td>
    <td align="right">5.72</td>
    <td align="right">5.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">9.34</td>
    <td align="right">11.39</td>
    <td align="right">7.01</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">9.14</td>
    <td align="right">9.73</td>
    <td align="right">7.18</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.13</td>
    <td align="right">9.40</td>
    <td align="right">6.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">11.22</td>
    <td align="right">12.71</td>
    <td align="right">8.73</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">14.15</td>
    <td align="right">16.70</td>
    <td align="right">11.70</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.47</td>
    <td align="right">20.73</td>
    <td align="right">10.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">3.40</td>
    <td align="right">3.34</td>
    <td align="right">3.34</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">4.67</td>
    <td align="right">5.34</td>
    <td align="right">5.39</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">4.68</td>
    <td align="right">5.31</td>
    <td align="right">5.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.49</td>
    <td align="right">3.34</td>
    <td align="right">3.44</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">4.61</td>
    <td align="right">5.75</td>
    <td align="right">5.17</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">4.80</td>
    <td align="right">5.27</td>
    <td align="right">5.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">8.72</td>
    <td align="right">11.17</td>
    <td align="right">6.74</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">8.28</td>
    <td align="right">9.58</td>
    <td align="right">7.33</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">9.32</td>
    <td align="right">9.72</td>
    <td align="right">6.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">13.39</td>
    <td align="right">14.83</td>
    <td align="right">10.33</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.87</td>
    <td align="right">19.31</td>
    <td align="right">11.79</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">14.98</td>
    <td align="right">17.46</td>
    <td align="right">11.31</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.58</td>
    <td align="right">3.97</td>
    <td align="right">3.64</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">7.95</td>
    <td align="right">5.12</td>
    <td align="right">12.59</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.68</td>
    <td align="right">1.31</td>
    <td align="right">1.28</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.84</td>
    <td align="right">1.53</td>
    <td align="right">1.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.26</td>
    <td align="right">9.23</td>
    <td align="right">13.52</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.58</td>
    <td align="right">1.51</td>
    <td align="right">1.80</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.81</td>
    <td align="right">1.69</td>
    <td align="right">1.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">15.49</td>
    <td align="right">9.98</td>
    <td align="right">12.76</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.85</td>
    <td align="right">2.11</td>
    <td align="right">1.88</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.99</td>
    <td align="right">1.84</td>
    <td align="right">1.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">22.08</td>
    <td align="right">12.76</td>
    <td align="right">12.45</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.86</td>
    <td align="right">3.90</td>
    <td align="right">2.46</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.97</td>
    <td align="right">1.81</td>
    <td align="right">2.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1818</td>
    <td align="right">8.19</td>
    <td align="right">4.79</td>
    <td align="right">13.26</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">1.41</td>
    <td align="right">1.37</td>
    <td align="right">1.53</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">1.82</td>
    <td align="right">1.55</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">11.34</td>
    <td align="right">6.90</td>
    <td align="right">13.55</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">1.55</td>
    <td align="right">1.86</td>
    <td align="right">2.06</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">1.84</td>
    <td align="right">1.63</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">14.05</td>
    <td align="right">8.43</td>
    <td align="right">12.63</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">1.76</td>
    <td align="right">1.85</td>
    <td align="right">2.37</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">1.91</td>
    <td align="right">1.84</td>
    <td align="right">1.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">18.11</td>
    <td align="right">11.62</td>
    <td align="right">13.00</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">2.65</td>
    <td align="right">2.23</td>
    <td align="right">1.98</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">1.92</td>
    <td align="right">1.95</td>
    <td align="right">1.85</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.65</td>
    <td align="right">1.87</td>
    <td align="right">1.79</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.53</td>
    <td align="right">2.34</td>
    <td align="right">2.06</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.17</td>
    <td align="right">1.83</td>
    <td align="right">1.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.68</td>
    <td align="right">2.68</td>
    <td align="right">2.31</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.11</td>
    <td align="right">2.59</td>
    <td align="right">2.35</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.03</td>
    <td align="right">1.75</td>
    <td align="right">1.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.77</td>
    <td align="right">3.19</td>
    <td align="right">3.47</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.66</td>
    <td align="right">3.51</td>
    <td align="right">3.28</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.63</td>
    <td align="right">3.06</td>
    <td align="right">2.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.33</td>
    <td align="right">5.18</td>
    <td align="right">4.85</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.56</td>
    <td align="right">4.71</td>
    <td align="right">5.23</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.52</td>
    <td align="right">3.89</td>
    <td align="right">2.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.51</td>
    <td align="right">1.90</td>
    <td align="right">1.94</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">2.61</td>
    <td align="right">1.97</td>
    <td align="right">2.22</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">2.16</td>
    <td align="right">1.89</td>
    <td align="right">1.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">2.51</td>
    <td align="right">2.49</td>
    <td align="right">2.53</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">2.97</td>
    <td align="right">2.34</td>
    <td align="right">2.42</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">1.61</td>
    <td align="right">2.10</td>
    <td align="right">1.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">4.58</td>
    <td align="right">3.27</td>
    <td align="right">3.24</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">5.02</td>
    <td align="right">3.42</td>
    <td align="right">3.74</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">3.41</td>
    <td align="right">2.70</td>
    <td align="right">2.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">5.48</td>
    <td align="right">4.78</td>
    <td align="right">4.48</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">5.45</td>
    <td align="right">4.32</td>
    <td align="right">4.51</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">3.19</td>
    <td align="right">4.14</td>
    <td align="right">2.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.31</td>
    <td align="right">1.93</td>
    <td align="right">1.94</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.77</td>
    <td align="right">1.92</td>
    <td align="right">2.41</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.99</td>
    <td align="right">2.07</td>
    <td align="right">2.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.40</td>
    <td align="right">2.22</td>
    <td align="right">2.27</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.39</td>
    <td align="right">2.49</td>
    <td align="right">3.60</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.23</td>
    <td align="right">3.34</td>
    <td align="right">2.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.27</td>
    <td align="right">3.23</td>
    <td align="right">2.14</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.67</td>
    <td align="right">3.34</td>
    <td align="right">3.47</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.70</td>
    <td align="right">6.16</td>
    <td align="right">3.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.38</td>
    <td align="right">3.57</td>
    <td align="right">2.28</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.82</td>
    <td align="right">6.03</td>
    <td align="right">4.82</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.28</td>
    <td align="right">5.88</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4739</td>
    <td align="right">2.68</td>
    <td align="right">2.07</td>
    <td align="right">1.95</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.48</td>
    <td align="right">2.38</td>
    <td align="right">2.69</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">2.61</td>
    <td align="right">2.05</td>
    <td align="right">2.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.01</td>
    <td align="right">2.34</td>
    <td align="right">1.91</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">2.92</td>
    <td align="right">2.53</td>
    <td align="right">3.01</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">3.44</td>
    <td align="right">2.70</td>
    <td align="right">3.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">4.01</td>
    <td align="right">4.65</td>
    <td align="right">2.36</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">6.03</td>
    <td align="right">3.34</td>
    <td align="right">4.31</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">4.97</td>
    <td align="right">6.01</td>
    <td align="right">4.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">6.24</td>
    <td align="right">4.52</td>
    <td align="right">2.79</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">7.98</td>
    <td align="right">6.41</td>
    <td align="right">5.13</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">6.75</td>
    <td align="right">5.25</td>
    <td align="right">5.85</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">33.14</td>
    <td align="right">18.11</td>
    <td align="right">11.40</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">12.40</td>
    <td align="right">13.28</td>
    <td align="right">22.50</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.56</td>
    <td align="right">2.25</td>
    <td align="right">5.08</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.07</td>
    <td align="right">4.30</td>
    <td align="right">4.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">32.12</td>
    <td align="right">31.70</td>
    <td align="right">30.42</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">12.63</td>
    <td align="right">10.49</td>
    <td align="right">7.12</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.85</td>
    <td align="right">9.12</td>
    <td align="right">10.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">65.96</td>
    <td align="right">46.78</td>
    <td align="right">28.16</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.96</td>
    <td align="right">11.35</td>
    <td align="right">10.23</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">13.40</td>
    <td align="right">10.98</td>
    <td align="right">10.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">85.95</td>
    <td align="right">73.01</td>
    <td align="right">33.85</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">16.63</td>
    <td align="right">15.98</td>
    <td align="right">14.28</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">14.87</td>
    <td align="right">11.80</td>
    <td align="right">14.01</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1556</td>
    <td align="right">18.57</td>
    <td align="right">18.46</td>
    <td align="right">25.12</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">6.86</td>
    <td align="right">7.99</td>
    <td align="right">8.26</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">6.39</td>
    <td align="right">7.50</td>
    <td align="right">6.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">52.16</td>
    <td align="right">43.96</td>
    <td align="right">31.96</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">8.72</td>
    <td align="right">7.82</td>
    <td align="right">7.78</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">7.22</td>
    <td align="right">7.99</td>
    <td align="right">8.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">48.40</td>
    <td align="right">43.67</td>
    <td align="right">25.51</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">11.35</td>
    <td align="right">9.02</td>
    <td align="right">10.08</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">12.63</td>
    <td align="right">10.14</td>
    <td align="right">9.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">63.78</td>
    <td align="right">49.99</td>
    <td align="right">20.65</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">8.46</td>
    <td align="right">7.50</td>
    <td align="right">8.24</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">7.62</td>
    <td align="right">7.27</td>
    <td align="right">6.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.24</td>
    <td align="right">3.20</td>
    <td align="right">2.92</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.79</td>
    <td align="right">4.81</td>
    <td align="right">4.67</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.27</td>
    <td align="right">4.58</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.31</td>
    <td align="right">9.64</td>
    <td align="right">9.73</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">13.39</td>
    <td align="right">11.21</td>
    <td align="right">10.38</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.78</td>
    <td align="right">7.32</td>
    <td align="right">7.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">17.98</td>
    <td align="right">15.20</td>
    <td align="right">15.36</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">15.80</td>
    <td align="right">13.21</td>
    <td align="right">13.31</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">10.09</td>
    <td align="right">11.68</td>
    <td align="right">8.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">20.95</td>
    <td align="right">14.86</td>
    <td align="right">13.37</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">14.91</td>
    <td align="right">13.65</td>
    <td align="right">13.71</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.10</td>
    <td align="right">10.52</td>
    <td align="right">6.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">3.07</td>
    <td align="right">2.85</td>
    <td align="right">2.59</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">2.82</td>
    <td align="right">2.68</td>
    <td align="right">2.64</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">2.46</td>
    <td align="right">2.61</td>
    <td align="right">2.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">3.73</td>
    <td align="right">4.22</td>
    <td align="right">4.09</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">4.08</td>
    <td align="right">4.54</td>
    <td align="right">4.54</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">2.62</td>
    <td align="right">3.66</td>
    <td align="right">3.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">9.71</td>
    <td align="right">8.89</td>
    <td align="right">8.87</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">9.73</td>
    <td align="right">8.64</td>
    <td align="right">8.82</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">7.43</td>
    <td align="right">7.76</td>
    <td align="right">5.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">20.19</td>
    <td align="right">14.79</td>
    <td align="right">14.62</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">17.06</td>
    <td align="right">14.86</td>
    <td align="right">14.73</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">10.96</td>
    <td align="right">10.82</td>
    <td align="right">6.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">2.62</td>
    <td align="right">2.98</td>
    <td align="right">3.04</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.18</td>
    <td align="right">3.11</td>
    <td align="right">3.01</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.95</td>
    <td align="right">2.68</td>
    <td align="right">2.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.39</td>
    <td align="right">3.00</td>
    <td align="right">4.05</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.86</td>
    <td align="right">4.28</td>
    <td align="right">4.28</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.09</td>
    <td align="right">4.63</td>
    <td align="right">4.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.30</td>
    <td align="right">7.55</td>
    <td align="right">5.26</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">9.71</td>
    <td align="right">8.91</td>
    <td align="right">8.86</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">9.66</td>
    <td align="right">8.95</td>
    <td align="right">8.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.52</td>
    <td align="right">10.36</td>
    <td align="right">6.12</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.41</td>
    <td align="right">13.67</td>
    <td align="right">14.26</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">14.77</td>
    <td align="right">13.70</td>
    <td align="right">13.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">2.44</td>
    <td align="right">2.60</td>
    <td align="right">2.56</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">2.75</td>
    <td align="right">2.63</td>
    <td align="right">2.58</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">2.93</td>
    <td align="right">2.97</td>
    <td align="right">2.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">2.83</td>
    <td align="right">3.04</td>
    <td align="right">2.98</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">3.76</td>
    <td align="right">4.72</td>
    <td align="right">4.07</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">4.10</td>
    <td align="right">4.78</td>
    <td align="right">4.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">7.51</td>
    <td align="right">7.54</td>
    <td align="right">5.16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">9.68</td>
    <td align="right">8.97</td>
    <td align="right">9.01</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">9.98</td>
    <td align="right">8.65</td>
    <td align="right">8.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">9.50</td>
    <td align="right">10.39</td>
    <td align="right">6.10</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">15.48</td>
    <td align="right">15.40</td>
    <td align="right">13.17</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">14.73</td>
    <td align="right">13.62</td>
    <td align="right">13.41</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">34.24</td>
    <td align="right">5.52</td>
    <td align="right">3.47</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.00</td>
    <td align="right">12.28</td>
    <td align="right">16.85</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.81</td>
    <td align="right">4.20</td>
    <td align="right">4.24</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.95</td>
    <td align="right">5.22</td>
    <td align="right">5.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.43</td>
    <td align="right">17.60</td>
    <td align="right">17.54</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.94</td>
    <td align="right">4.88</td>
    <td align="right">4.73</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.03</td>
    <td align="right">5.89</td>
    <td align="right">5.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.72</td>
    <td align="right">21.24</td>
    <td align="right">16.56</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.59</td>
    <td align="right">5.44</td>
    <td align="right">5.47</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.31</td>
    <td align="right">6.50</td>
    <td align="right">6.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.29</td>
    <td align="right">27.57</td>
    <td align="right">17.27</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.96</td>
    <td align="right">5.90</td>
    <td align="right">5.90</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.37</td>
    <td align="right">7.36</td>
    <td align="right">7.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1818</td>
    <td align="right">13.49</td>
    <td align="right">13.35</td>
    <td align="right">17.93</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">6.00</td>
    <td align="right">4.35</td>
    <td align="right">4.50</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">7.11</td>
    <td align="right">5.68</td>
    <td align="right">5.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">20.71</td>
    <td align="right">19.41</td>
    <td align="right">18.64</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">7.21</td>
    <td align="right">4.90</td>
    <td align="right">5.04</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">8.39</td>
    <td align="right">6.11</td>
    <td align="right">6.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">26.30</td>
    <td align="right">24.03</td>
    <td align="right">17.74</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">8.93</td>
    <td align="right">5.54</td>
    <td align="right">5.73</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">9.65</td>
    <td align="right">6.78</td>
    <td align="right">6.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">34.42</td>
    <td align="right">30.71</td>
    <td align="right">18.14</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">10.14</td>
    <td align="right">6.05</td>
    <td align="right">6.27</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">11.11</td>
    <td align="right">7.66</td>
    <td align="right">7.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.91</td>
    <td align="right">5.64</td>
    <td align="right">5.68</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.23</td>
    <td align="right">5.54</td>
    <td align="right">5.52</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.34</td>
    <td align="right">3.92</td>
    <td align="right">3.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.72</td>
    <td align="right">8.45</td>
    <td align="right">9.21</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.31</td>
    <td align="right">8.71</td>
    <td align="right">8.69</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.89</td>
    <td align="right">4.84</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.63</td>
    <td align="right">10.96</td>
    <td align="right">10.75</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.97</td>
    <td align="right">10.46</td>
    <td align="right">10.45</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.93</td>
    <td align="right">6.97</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">17.47</td>
    <td align="right">13.95</td>
    <td align="right">13.91</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.79</td>
    <td align="right">13.39</td>
    <td align="right">12.74</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.00</td>
    <td align="right">7.05</td>
    <td align="right">5.31</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.94</td>
    <td align="right">5.71</td>
    <td align="right">5.70</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">9.22</td>
    <td align="right">5.41</td>
    <td align="right">5.37</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">3.41</td>
    <td align="right">3.97</td>
    <td align="right">3.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">11.19</td>
    <td align="right">8.70</td>
    <td align="right">8.68</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">15.31</td>
    <td align="right">8.74</td>
    <td align="right">7.84</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.93</td>
    <td align="right">4.88</td>
    <td align="right">4.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">15.67</td>
    <td align="right">11.08</td>
    <td align="right">11.36</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">16.09</td>
    <td align="right">10.72</td>
    <td align="right">10.72</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">5.22</td>
    <td align="right">7.18</td>
    <td align="right">5.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">17.58</td>
    <td align="right">14.54</td>
    <td align="right">14.39</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">18.82</td>
    <td align="right">13.70</td>
    <td align="right">13.64</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">5.30</td>
    <td align="right">7.15</td>
    <td align="right">5.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.31</td>
    <td align="right">3.83</td>
    <td align="right">3.82</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.46</td>
    <td align="right">5.50</td>
    <td align="right">5.51</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.61</td>
    <td align="right">5.38</td>
    <td align="right">5.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.24</td>
    <td align="right">5.55</td>
    <td align="right">4.67</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.75</td>
    <td align="right">5.81</td>
    <td align="right">5.05</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.93</td>
    <td align="right">6.93</td>
    <td align="right">6.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.03</td>
    <td align="right">6.84</td>
    <td align="right">5.09</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.74</td>
    <td align="right">9.31</td>
    <td align="right">7.59</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.74</td>
    <td align="right">9.31</td>
    <td align="right">7.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.08</td>
    <td align="right">6.92</td>
    <td align="right">5.05</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.30</td>
    <td align="right">10.61</td>
    <td align="right">7.72</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.08</td>
    <td align="right">10.28</td>
    <td align="right">7.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4739</td>
    <td align="right">3.31</td>
    <td align="right">3.93</td>
    <td align="right">3.89</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">4.47</td>
    <td align="right">5.52</td>
    <td align="right">5.53</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">4.62</td>
    <td align="right">5.37</td>
    <td align="right">5.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.28</td>
    <td align="right">5.50</td>
    <td align="right">4.63</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">4.77</td>
    <td align="right">5.91</td>
    <td align="right">5.10</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">6.99</td>
    <td align="right">7.09</td>
    <td align="right">6.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">5.00</td>
    <td align="right">6.85</td>
    <td align="right">5.15</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">9.82</td>
    <td align="right">9.46</td>
    <td align="right">7.77</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">9.70</td>
    <td align="right">9.15</td>
    <td align="right">7.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">5.07</td>
    <td align="right">6.90</td>
    <td align="right">5.11</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">10.12</td>
    <td align="right">10.57</td>
    <td align="right">7.76</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">10.26</td>
    <td align="right">10.37</td>
    <td align="right">7.64</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">42.02</td>
    <td align="right">20.17</td>
    <td align="right">8.76</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.49</td>
    <td align="right">13.10</td>
    <td align="right">17.62</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.00</td>
    <td align="right">4.50</td>
    <td align="right">4.47</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.87</td>
    <td align="right">5.52</td>
    <td align="right">5.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.80</td>
    <td align="right">19.22</td>
    <td align="right">18.47</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.02</td>
    <td align="right">5.20</td>
    <td align="right">5.26</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.56</td>
    <td align="right">6.58</td>
    <td align="right">6.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">32.60</td>
    <td align="right">26.54</td>
    <td align="right">19.10</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">13.19</td>
    <td align="right">6.68</td>
    <td align="right">6.88</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">13.58</td>
    <td align="right">8.24</td>
    <td align="right">8.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">54.05</td>
    <td align="right">56.19</td>
    <td align="right">20.99</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">17.60</td>
    <td align="right">12.25</td>
    <td align="right">11.68</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">17.73</td>
    <td align="right">14.57</td>
    <td align="right">15.06</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1556</td>
    <td align="right">15.78</td>
    <td align="right">14.43</td>
    <td align="right">18.96</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">7.23</td>
    <td align="right">4.63</td>
    <td align="right">4.65</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">8.55</td>
    <td align="right">6.06</td>
    <td align="right">5.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">24.67</td>
    <td align="right">21.20</td>
    <td align="right">19.85</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">9.56</td>
    <td align="right">5.91</td>
    <td align="right">6.80</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">10.34</td>
    <td align="right">6.59</td>
    <td align="right">6.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">37.05</td>
    <td align="right">40.85</td>
    <td align="right">22.48</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">14.49</td>
    <td align="right">9.85</td>
    <td align="right">7.95</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">13.95</td>
    <td align="right">9.09</td>
    <td align="right">8.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">59.40</td>
    <td align="right">59.21</td>
    <td align="right">22.14</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">17.24</td>
    <td align="right">12.30</td>
    <td align="right">12.86</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">19.79</td>
    <td align="right">14.59</td>
    <td align="right">14.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.32</td>
    <td align="right">6.30</td>
    <td align="right">6.28</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.45</td>
    <td align="right">6.26</td>
    <td align="right">6.24</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.70</td>
    <td align="right">4.18</td>
    <td align="right">4.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.40</td>
    <td align="right">10.06</td>
    <td align="right">10.48</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">19.19</td>
    <td align="right">9.83</td>
    <td align="right">9.36</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.27</td>
    <td align="right">5.30</td>
    <td align="right">5.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">20.53</td>
    <td align="right">14.24</td>
    <td align="right">15.77</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">20.62</td>
    <td align="right">15.23</td>
    <td align="right">12.71</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.11</td>
    <td align="right">11.27</td>
    <td align="right">7.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">26.58</td>
    <td align="right">23.00</td>
    <td align="right">23.77</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">28.65</td>
    <td align="right">20.80</td>
    <td align="right">21.15</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">14.00</td>
    <td align="right">17.64</td>
    <td align="right">14.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">9.45</td>
    <td align="right">6.37</td>
    <td align="right">6.37</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">9.52</td>
    <td align="right">5.90</td>
    <td align="right">5.70</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.68</td>
    <td align="right">4.29</td>
    <td align="right">4.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">17.36</td>
    <td align="right">13.35</td>
    <td align="right">12.49</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">23.96</td>
    <td align="right">13.06</td>
    <td align="right">10.10</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">3.27</td>
    <td align="right">6.68</td>
    <td align="right">4.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">27.62</td>
    <td align="right">23.35</td>
    <td align="right">15.90</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">26.39</td>
    <td align="right">17.70</td>
    <td align="right">13.33</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">6.86</td>
    <td align="right">10.42</td>
    <td align="right">7.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">25.68</td>
    <td align="right">23.34</td>
    <td align="right">23.37</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">27.63</td>
    <td align="right">21.18</td>
    <td align="right">19.70</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">12.58</td>
    <td align="right">20.77</td>
    <td align="right">16.10</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.70</td>
    <td align="right">4.06</td>
    <td align="right">4.06</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.96</td>
    <td align="right">5.97</td>
    <td align="right">5.92</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.03</td>
    <td align="right">5.82</td>
    <td align="right">5.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.69</td>
    <td align="right">6.18</td>
    <td align="right">5.37</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.62</td>
    <td align="right">6.45</td>
    <td align="right">5.71</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.81</td>
    <td align="right">7.66</td>
    <td align="right">6.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.01</td>
    <td align="right">8.82</td>
    <td align="right">6.50</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">12.13</td>
    <td align="right">11.95</td>
    <td align="right">9.59</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">11.63</td>
    <td align="right">10.73</td>
    <td align="right">8.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">11.35</td>
    <td align="right">16.99</td>
    <td align="right">10.84</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">14.16</td>
    <td align="right">16.88</td>
    <td align="right">11.58</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">15.94</td>
    <td align="right">17.38</td>
    <td align="right">12.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">3.64</td>
    <td align="right">4.14</td>
    <td align="right">4.14</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">5.07</td>
    <td align="right">5.88</td>
    <td align="right">5.91</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">5.16</td>
    <td align="right">5.81</td>
    <td align="right">5.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.70</td>
    <td align="right">5.99</td>
    <td align="right">5.06</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">5.68</td>
    <td align="right">6.57</td>
    <td align="right">5.56</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">7.80</td>
    <td align="right">7.92</td>
    <td align="right">6.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">6.69</td>
    <td align="right">8.92</td>
    <td align="right">6.44</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">11.52</td>
    <td align="right">11.27</td>
    <td align="right">9.04</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">11.58</td>
    <td align="right">11.63</td>
    <td align="right">8.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">9.98</td>
    <td align="right">14.69</td>
    <td align="right">10.18</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.35</td>
    <td align="right">18.49</td>
    <td align="right">12.26</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">14.68</td>
    <td align="right">14.25</td>
    <td align="right">10.24</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.94</td>
    <td align="right">30.06</td>
    <td align="right">13.89</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.65</td>
    <td align="right">41.97</td>
    <td align="right">36.50</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.52</td>
    <td align="right">15.94</td>
    <td align="right">15.94</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.17</td>
    <td align="right">19.68</td>
    <td align="right">19.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">36.97</td>
    <td align="right">63.29</td>
    <td align="right">39.19</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.26</td>
    <td align="right">19.37</td>
    <td align="right">19.21</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.08</td>
    <td align="right">18.54</td>
    <td align="right">18.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.51</td>
    <td align="right">77.28</td>
    <td align="right">38.10</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.16</td>
    <td align="right">18.39</td>
    <td align="right">18.42</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.04</td>
    <td align="right">18.28</td>
    <td align="right">18.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">56.19</td>
    <td align="right">96.25</td>
    <td align="right">37.39</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.12</td>
    <td align="right">19.01</td>
    <td align="right">18.76</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.94</td>
    <td align="right">19.95</td>
    <td align="right">19.95</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1768</td>
    <td align="right">27.87</td>
    <td align="right">39.97</td>
    <td align="right">37.08</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">12.24</td>
    <td align="right">15.52</td>
    <td align="right">15.48</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">13.72</td>
    <td align="right">16.14</td>
    <td align="right">16.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">42.51</td>
    <td align="right">58.93</td>
    <td align="right">39.43</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">14.45</td>
    <td align="right">17.06</td>
    <td align="right">17.16</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">15.04</td>
    <td align="right">17.22</td>
    <td align="right">17.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">51.16</td>
    <td align="right">72.80</td>
    <td align="right">38.55</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">14.67</td>
    <td align="right">17.58</td>
    <td align="right">17.59</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">16.63</td>
    <td align="right">17.49</td>
    <td align="right">17.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">65.39</td>
    <td align="right">98.19</td>
    <td align="right">41.20</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">16.40</td>
    <td align="right">17.73</td>
    <td align="right">18.37</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">15.84</td>
    <td align="right">19.11</td>
    <td align="right">19.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.07</td>
    <td align="right">20.44</td>
    <td align="right">20.43</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.54</td>
    <td align="right">22.15</td>
    <td align="right">22.18</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.51</td>
    <td align="right">13.55</td>
    <td align="right">13.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.29</td>
    <td align="right">26.72</td>
    <td align="right">26.78</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.57</td>
    <td align="right">28.88</td>
    <td align="right">28.95</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.83</td>
    <td align="right">16.51</td>
    <td align="right">15.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.99</td>
    <td align="right">33.14</td>
    <td align="right">33.14</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.58</td>
    <td align="right">45.91</td>
    <td align="right">45.83</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.69</td>
    <td align="right">19.58</td>
    <td align="right">19.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.65</td>
    <td align="right">36.37</td>
    <td align="right">36.21</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.63</td>
    <td align="right">55.53</td>
    <td align="right">55.54</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.52</td>
    <td align="right">24.84</td>
    <td align="right">24.79</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">17.31</td>
    <td align="right">20.70</td>
    <td align="right">20.79</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">29.32</td>
    <td align="right">20.83</td>
    <td align="right">20.78</td>
    <td align="center">5</td>
    <td align="right">2.7323</td>
    <td align="right">11.40</td>
    <td align="right">14.31</td>
    <td align="right">14.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">21.28</td>
    <td align="right">26.68</td>
    <td align="right">26.65</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">40.13</td>
    <td align="right">27.80</td>
    <td align="right">27.77</td>
    <td align="center">8</td>
    <td align="right">0.5321</td>
    <td align="right">13.72</td>
    <td align="right">18.19</td>
    <td align="right">18.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">30.14</td>
    <td align="right">34.54</td>
    <td align="right">33.99</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">66.04</td>
    <td align="right">46.26</td>
    <td align="right">46.27</td>
    <td align="center">11</td>
    <td align="right">0.1189</td>
    <td align="right">16.30</td>
    <td align="right">19.89</td>
    <td align="right">19.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">34.86</td>
    <td align="right">36.82</td>
    <td align="right">36.64</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">78.15</td>
    <td align="right">55.52</td>
    <td align="right">55.13</td>
    <td align="center">13</td>
    <td align="right">0.0298</td>
    <td align="right">25.77</td>
    <td align="right">25.63</td>
    <td align="right">25.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">14.52</td>
    <td align="right">16.08</td>
    <td align="right">15.66</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.22</td>
    <td align="right">20.77</td>
    <td align="right">20.66</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.90</td>
    <td align="right">22.30</td>
    <td align="right">22.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.28</td>
    <td align="right">20.46</td>
    <td align="right">20.35</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.53</td>
    <td align="right">26.87</td>
    <td align="right">26.89</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.98</td>
    <td align="right">29.05</td>
    <td align="right">29.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.98</td>
    <td align="right">25.03</td>
    <td align="right">25.12</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.31</td>
    <td align="right">33.28</td>
    <td align="right">33.54</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.23</td>
    <td align="right">46.13</td>
    <td align="right">46.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">34.50</td>
    <td align="right">35.17</td>
    <td align="right">35.07</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.53</td>
    <td align="right">36.48</td>
    <td align="right">36.54</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.99</td>
    <td align="right">55.57</td>
    <td align="right">55.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4960</td>
    <td align="right">15.10</td>
    <td align="right">16.09</td>
    <td align="right">16.08</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">17.57</td>
    <td align="right">20.74</td>
    <td align="right">20.81</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">29.50</td>
    <td align="right">20.95</td>
    <td align="right">21.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4318</td>
    <td align="right">20.34</td>
    <td align="right">20.45</td>
    <td align="right">20.50</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">21.51</td>
    <td align="right">26.87</td>
    <td align="right">26.87</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">40.65</td>
    <td align="right">28.02</td>
    <td align="right">27.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0968</td>
    <td align="right">28.92</td>
    <td align="right">23.52</td>
    <td align="right">23.59</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">30.49</td>
    <td align="right">35.01</td>
    <td align="right">34.51</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">66.39</td>
    <td align="right">46.57</td>
    <td align="right">46.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">35.03</td>
    <td align="right">35.41</td>
    <td align="right">35.15</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">35.24</td>
    <td align="right">36.98</td>
    <td align="right">37.21</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">78.84</td>
    <td align="right">55.12</td>
    <td align="right">55.56</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">92.24</td>
    <td align="right">117.08</td>
    <td align="right">29.14</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">28.51</td>
    <td align="right">47.85</td>
    <td align="right">41.53</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">15.03</td>
    <td align="right">17.33</td>
    <td align="right">17.61</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">17.75</td>
    <td align="right">26.57</td>
    <td align="right">28.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">38.96</td>
    <td align="right">76.98</td>
    <td align="right">45.80</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">23.21</td>
    <td align="right">21.95</td>
    <td align="right">23.38</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">18.38</td>
    <td align="right">20.57</td>
    <td align="right">21.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">63.01</td>
    <td align="right">112.52</td>
    <td align="right">53.90</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">27.58</td>
    <td align="right">38.41</td>
    <td align="right">42.62</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">31.40</td>
    <td align="right">23.87</td>
    <td align="right">26.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">180.80</td>
    <td align="right">238.02</td>
    <td align="right">89.02</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">56.58</td>
    <td align="right">58.25</td>
    <td align="right">55.76</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">56.87</td>
    <td align="right">56.42</td>
    <td align="right">53.76</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1542</td>
    <td align="right">32.99</td>
    <td align="right">64.33</td>
    <td align="right">71.01</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">13.34</td>
    <td align="right">17.18</td>
    <td align="right">17.87</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">14.34</td>
    <td align="right">16.79</td>
    <td align="right">16.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">46.97</td>
    <td align="right">68.26</td>
    <td align="right">50.18</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">37.88</td>
    <td align="right">35.02</td>
    <td align="right">19.39</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">17.77</td>
    <td align="right">20.75</td>
    <td align="right">20.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">87.59</td>
    <td align="right">106.96</td>
    <td align="right">60.10</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">28.09</td>
    <td align="right">32.49</td>
    <td align="right">30.67</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">24.87</td>
    <td align="right">29.83</td>
    <td align="right">24.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">170.76</td>
    <td align="right">265.26</td>
    <td align="right">80.35</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">38.32</td>
    <td align="right">36.54</td>
    <td align="right">38.71</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">33.31</td>
    <td align="right">41.93</td>
    <td align="right">44.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">18.46</td>
    <td align="right">22.34</td>
    <td align="right">21.70</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">35.50</td>
    <td align="right">24.02</td>
    <td align="right">24.02</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">11.13</td>
    <td align="right">14.20</td>
    <td align="right">14.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">24.50</td>
    <td align="right">29.76</td>
    <td align="right">29.21</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">58.05</td>
    <td align="right">38.13</td>
    <td align="right">40.96</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">13.60</td>
    <td align="right">17.73</td>
    <td align="right">17.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">44.42</td>
    <td align="right">65.55</td>
    <td align="right">54.12</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">92.77</td>
    <td align="right">58.88</td>
    <td align="right">63.12</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">35.30</td>
    <td align="right">49.22</td>
    <td align="right">40.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">63.99</td>
    <td align="right">79.12</td>
    <td align="right">76.49</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">111.64</td>
    <td align="right">92.70</td>
    <td align="right">98.45</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">53.38</td>
    <td align="right">52.96</td>
    <td align="right">51.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">18.34</td>
    <td align="right">24.44</td>
    <td align="right">22.37</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">35.61</td>
    <td align="right">24.18</td>
    <td align="right">23.53</td>
    <td align="center">5</td>
    <td align="right">2.7367</td>
    <td align="right">11.91</td>
    <td align="right">15.05</td>
    <td align="right">15.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">28.26</td>
    <td align="right">30.06</td>
    <td align="right">35.41</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">57.76</td>
    <td align="right">36.38</td>
    <td align="right">40.23</td>
    <td align="center">8</td>
    <td align="right">0.5431</td>
    <td align="right">14.64</td>
    <td align="right">22.69</td>
    <td align="right">21.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">53.28</td>
    <td align="right">68.48</td>
    <td align="right">61.01</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">86.10</td>
    <td align="right">62.37</td>
    <td align="right">58.43</td>
    <td align="center">11</td>
    <td align="right">0.1181</td>
    <td align="right">32.73</td>
    <td align="right">34.90</td>
    <td align="right">38.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">75.00</td>
    <td align="right">103.19</td>
    <td align="right">102.93</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">132.89</td>
    <td align="right">111.09</td>
    <td align="right">105.02</td>
    <td align="center">13</td>
    <td align="right">0.0278</td>
    <td align="right">62.29</td>
    <td align="right">74.28</td>
    <td align="right">79.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">16.80</td>
    <td align="right">18.60</td>
    <td align="right">17.36</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">19.35</td>
    <td align="right">23.70</td>
    <td align="right">23.32</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">41.55</td>
    <td align="right">26.00</td>
    <td align="right">27.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">28.18</td>
    <td align="right">32.89</td>
    <td align="right">35.86</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">31.99</td>
    <td align="right">42.14</td>
    <td align="right">40.98</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">73.79</td>
    <td align="right">47.68</td>
    <td align="right">48.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">81.05</td>
    <td align="right">48.64</td>
    <td align="right">51.93</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">62.08</td>
    <td align="right">81.13</td>
    <td align="right">65.15</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">102.73</td>
    <td align="right">77.92</td>
    <td align="right">72.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">92.46</td>
    <td align="right">97.18</td>
    <td align="right">99.08</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">74.36</td>
    <td align="right">83.99</td>
    <td align="right">68.44</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">107.39</td>
    <td align="right">85.91</td>
    <td align="right">91.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">16.25</td>
    <td align="right">16.80</td>
    <td align="right">17.35</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">22.27</td>
    <td align="right">23.42</td>
    <td align="right">23.44</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">45.66</td>
    <td align="right">23.16</td>
    <td align="right">22.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4426</td>
    <td align="right">22.13</td>
    <td align="right">22.00</td>
    <td align="right">28.58</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">32.05</td>
    <td align="right">30.45</td>
    <td align="right">29.96</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">54.54</td>
    <td align="right">35.22</td>
    <td align="right">34.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0868</td>
    <td align="right">56.76</td>
    <td align="right">37.34</td>
    <td align="right">37.92</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">47.93</td>
    <td align="right">67.04</td>
    <td align="right">71.56</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">78.95</td>
    <td align="right">54.78</td>
    <td align="right">58.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">78.26</td>
    <td align="right">74.76</td>
    <td align="right">80.30</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">56.71</td>
    <td align="right">64.63</td>
    <td align="right">62.12</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">103.22</td>
    <td align="right">77.71</td>
    <td align="right">71.54</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">62.07</td>
    <td align="right">10.21</td>
    <td align="right">6.88</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">13.74</td>
    <td align="right">22.58</td>
    <td align="right">26.43</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.48</td>
    <td align="right">12.29</td>
    <td align="right">12.30</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.62</td>
    <td align="right">13.81</td>
    <td align="right">13.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.35</td>
    <td align="right">34.79</td>
    <td align="right">28.72</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.09</td>
    <td align="right">14.06</td>
    <td align="right">14.08</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.46</td>
    <td align="right">15.30</td>
    <td align="right">15.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.87</td>
    <td align="right">47.26</td>
    <td align="right">30.04</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.80</td>
    <td align="right">15.32</td>
    <td align="right">15.38</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.54</td>
    <td align="right">16.71</td>
    <td align="right">16.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">32.45</td>
    <td align="right">60.26</td>
    <td align="right">30.85</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.57</td>
    <td align="right">16.25</td>
    <td align="right">16.25</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.88</td>
    <td align="right">17.83</td>
    <td align="right">17.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1768</td>
    <td align="right">19.15</td>
    <td align="right">27.81</td>
    <td align="right">28.31</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">9.57</td>
    <td align="right">12.41</td>
    <td align="right">12.39</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">12.58</td>
    <td align="right">14.62</td>
    <td align="right">14.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">28.16</td>
    <td align="right">41.78</td>
    <td align="right">30.74</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">13.02</td>
    <td align="right">14.96</td>
    <td align="right">14.94</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">14.39</td>
    <td align="right">15.86</td>
    <td align="right">15.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">34.79</td>
    <td align="right">53.42</td>
    <td align="right">30.12</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">14.57</td>
    <td align="right">16.19</td>
    <td align="right">16.21</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">15.27</td>
    <td align="right">17.19</td>
    <td align="right">17.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">47.99</td>
    <td align="right">67.53</td>
    <td align="right">31.69</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">15.46</td>
    <td align="right">17.28</td>
    <td align="right">17.28</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">16.71</td>
    <td align="right">18.98</td>
    <td align="right">19.23</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.59</td>
    <td align="right">16.03</td>
    <td align="right">16.02</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.26</td>
    <td align="right">16.65</td>
    <td align="right">16.65</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.12</td>
    <td align="right">9.32</td>
    <td align="right">9.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.30</td>
    <td align="right">22.43</td>
    <td align="right">22.42</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.27</td>
    <td align="right">22.31</td>
    <td align="right">22.31</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">10.72</td>
    <td align="right">13.93</td>
    <td align="right">13.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.81</td>
    <td align="right">32.03</td>
    <td align="right">31.97</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.52</td>
    <td align="right">30.51</td>
    <td align="right">30.71</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.74</td>
    <td align="right">17.51</td>
    <td align="right">17.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.72</td>
    <td align="right">35.59</td>
    <td align="right">35.53</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.52</td>
    <td align="right">36.12</td>
    <td align="right">35.75</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.25</td>
    <td align="right">20.41</td>
    <td align="right">20.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">13.23</td>
    <td align="right">16.81</td>
    <td align="right">16.76</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">14.20</td>
    <td align="right">16.33</td>
    <td align="right">16.32</td>
    <td align="center">5</td>
    <td align="right">2.7323</td>
    <td align="right">7.20</td>
    <td align="right">9.42</td>
    <td align="right">9.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">17.89</td>
    <td align="right">25.29</td>
    <td align="right">25.26</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">19.47</td>
    <td align="right">23.64</td>
    <td align="right">23.65</td>
    <td align="center">8</td>
    <td align="right">0.5321</td>
    <td align="right">10.90</td>
    <td align="right">13.42</td>
    <td align="right">13.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">24.92</td>
    <td align="right">32.55</td>
    <td align="right">32.31</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">27.91</td>
    <td align="right">31.11</td>
    <td align="right">30.84</td>
    <td align="center">11</td>
    <td align="right">0.1189</td>
    <td align="right">13.14</td>
    <td align="right">17.80</td>
    <td align="right">17.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">28.28</td>
    <td align="right">35.87</td>
    <td align="right">35.86</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">34.13</td>
    <td align="right">38.06</td>
    <td align="right">38.10</td>
    <td align="center">13</td>
    <td align="right">0.0298</td>
    <td align="right">17.34</td>
    <td align="right">20.68</td>
    <td align="right">20.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">6.54</td>
    <td align="right">9.33</td>
    <td align="right">9.33</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.71</td>
    <td align="right">16.04</td>
    <td align="right">16.03</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.27</td>
    <td align="right">16.68</td>
    <td align="right">16.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">12.36</td>
    <td align="right">13.68</td>
    <td align="right">13.67</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.32</td>
    <td align="right">22.47</td>
    <td align="right">22.47</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.28</td>
    <td align="right">22.31</td>
    <td align="right">22.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.82</td>
    <td align="right">17.59</td>
    <td align="right">17.57</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.84</td>
    <td align="right">32.04</td>
    <td align="right">32.00</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.54</td>
    <td align="right">30.53</td>
    <td align="right">30.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.06</td>
    <td align="right">20.98</td>
    <td align="right">20.91</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.69</td>
    <td align="right">35.55</td>
    <td align="right">35.53</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.14</td>
    <td align="right">35.75</td>
    <td align="right">35.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4960</td>
    <td align="right">6.73</td>
    <td align="right">9.47</td>
    <td align="right">9.44</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">13.46</td>
    <td align="right">16.83</td>
    <td align="right">16.80</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">14.25</td>
    <td align="right">16.25</td>
    <td align="right">16.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4318</td>
    <td align="right">10.60</td>
    <td align="right">13.79</td>
    <td align="right">13.79</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">17.90</td>
    <td align="right">25.74</td>
    <td align="right">25.46</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">19.45</td>
    <td align="right">23.71</td>
    <td align="right">23.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0968</td>
    <td align="right">14.34</td>
    <td align="right">17.52</td>
    <td align="right">17.43</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">25.02</td>
    <td align="right">32.58</td>
    <td align="right">32.32</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">27.64</td>
    <td align="right">31.13</td>
    <td align="right">30.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">17.66</td>
    <td align="right">20.60</td>
    <td align="right">20.64</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">28.27</td>
    <td align="right">35.87</td>
    <td align="right">35.86</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">34.15</td>
    <td align="right">38.08</td>
    <td align="right">38.07</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">77.74</td>
    <td align="right">44.05</td>
    <td align="right">10.24</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">14.26</td>
    <td align="right">23.18</td>
    <td align="right">28.46</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.73</td>
    <td align="right">12.72</td>
    <td align="right">12.69</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">11.95</td>
    <td align="right">14.11</td>
    <td align="right">14.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.33</td>
    <td align="right">34.56</td>
    <td align="right">29.32</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">11.97</td>
    <td align="right">13.81</td>
    <td align="right">13.86</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.39</td>
    <td align="right">15.00</td>
    <td align="right">15.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.68</td>
    <td align="right">47.60</td>
    <td align="right">32.86</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">18.15</td>
    <td align="right">19.13</td>
    <td align="right">17.68</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">14.37</td>
    <td align="right">16.37</td>
    <td align="right">16.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">33.08</td>
    <td align="right">62.71</td>
    <td align="right">31.23</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">14.91</td>
    <td align="right">16.47</td>
    <td align="right">16.24</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">16.29</td>
    <td align="right">17.85</td>
    <td align="right">18.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1542</td>
    <td align="right">19.74</td>
    <td align="right">28.54</td>
    <td align="right">30.52</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">9.83</td>
    <td align="right">12.80</td>
    <td align="right">13.05</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">12.93</td>
    <td align="right">14.89</td>
    <td align="right">14.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">27.67</td>
    <td align="right">40.89</td>
    <td align="right">31.48</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">12.88</td>
    <td align="right">14.69</td>
    <td align="right">14.71</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">14.22</td>
    <td align="right">15.54</td>
    <td align="right">15.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">33.87</td>
    <td align="right">52.29</td>
    <td align="right">30.21</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">14.35</td>
    <td align="right">15.82</td>
    <td align="right">16.82</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">16.05</td>
    <td align="right">18.50</td>
    <td align="right">16.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">53.31</td>
    <td align="right">69.31</td>
    <td align="right">31.94</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">15.45</td>
    <td align="right">18.57</td>
    <td align="right">18.73</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">17.00</td>
    <td align="right">20.67</td>
    <td align="right">19.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.85</td>
    <td align="right">17.02</td>
    <td align="right">17.03</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.61</td>
    <td align="right">17.85</td>
    <td align="right">17.85</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.40</td>
    <td align="right">9.74</td>
    <td align="right">9.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.04</td>
    <td align="right">22.02</td>
    <td align="right">22.01</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.62</td>
    <td align="right">22.31</td>
    <td align="right">22.45</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.21</td>
    <td align="right">14.53</td>
    <td align="right">14.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">30.27</td>
    <td align="right">48.81</td>
    <td align="right">46.75</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">50.20</td>
    <td align="right">34.50</td>
    <td align="right">33.47</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">22.67</td>
    <td align="right">21.76</td>
    <td align="right">17.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">29.55</td>
    <td align="right">39.02</td>
    <td align="right">83.96</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">72.10</td>
    <td align="right">123.20</td>
    <td align="right">105.63</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">21.79</td>
    <td align="right">29.04</td>
    <td align="right">29.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">13.69</td>
    <td align="right">17.49</td>
    <td align="right">17.34</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">15.15</td>
    <td align="right">17.04</td>
    <td align="right">16.86</td>
    <td align="center">5</td>
    <td align="right">2.7367</td>
    <td align="right">7.36</td>
    <td align="right">9.75</td>
    <td align="right">9.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">17.93</td>
    <td align="right">24.41</td>
    <td align="right">24.34</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">19.80</td>
    <td align="right">22.74</td>
    <td align="right">23.10</td>
    <td align="center">8</td>
    <td align="right">0.5431</td>
    <td align="right">11.13</td>
    <td align="right">13.18</td>
    <td align="right">13.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">25.54</td>
    <td align="right">35.56</td>
    <td align="right">39.05</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">31.73</td>
    <td align="right">34.08</td>
    <td align="right">37.43</td>
    <td align="center">11</td>
    <td align="right">0.1181</td>
    <td align="right">21.38</td>
    <td align="right">52.33</td>
    <td align="right">50.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">33.39</td>
    <td align="right">63.19</td>
    <td align="right">74.09</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">83.05</td>
    <td align="right">41.58</td>
    <td align="right">63.76</td>
    <td align="center">13</td>
    <td align="right">0.0278</td>
    <td align="right">21.30</td>
    <td align="right">37.58</td>
    <td align="right">28.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">6.87</td>
    <td align="right">9.83</td>
    <td align="right">9.83</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.84</td>
    <td align="right">17.02</td>
    <td align="right">17.07</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.63</td>
    <td align="right">18.03</td>
    <td align="right">18.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">11.98</td>
    <td align="right">14.61</td>
    <td align="right">13.41</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.13</td>
    <td align="right">22.13</td>
    <td align="right">22.45</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.56</td>
    <td align="right">23.65</td>
    <td align="right">28.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">12.91</td>
    <td align="right">17.63</td>
    <td align="right">17.24</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.85</td>
    <td align="right">36.50</td>
    <td align="right">36.11</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">26.24</td>
    <td align="right">31.64</td>
    <td align="right">31.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">31.60</td>
    <td align="right">24.19</td>
    <td align="right">24.76</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">28.59</td>
    <td align="right">49.32</td>
    <td align="right">57.76</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">40.32</td>
    <td align="right">38.60</td>
    <td align="right">41.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4684</td>
    <td align="right">8.87</td>
    <td align="right">9.88</td>
    <td align="right">9.87</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">13.82</td>
    <td align="right">17.54</td>
    <td align="right">17.33</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">14.75</td>
    <td align="right">16.73</td>
    <td align="right">16.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4426</td>
    <td align="right">11.33</td>
    <td align="right">13.57</td>
    <td align="right">13.50</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">21.72</td>
    <td align="right">26.25</td>
    <td align="right">25.79</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">19.99</td>
    <td align="right">24.49</td>
    <td align="right">25.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0868</td>
    <td align="right">15.55</td>
    <td align="right">19.91</td>
    <td align="right">21.31</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">26.62</td>
    <td align="right">36.33</td>
    <td align="right">40.26</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">28.60</td>
    <td align="right">32.43</td>
    <td align="right">34.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">21.25</td>
    <td align="right">23.88</td>
    <td align="right">23.69</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">31.03</td>
    <td align="right">43.38</td>
    <td align="right">42.57</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">36.58</td>
    <td align="right">40.44</td>
    <td align="right">43.79</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">44.77</td>
    <td align="right">9.52</td>
    <td align="right">6.71</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">59.79</td>
    <td align="right">55.85</td>
    <td align="right">41.98</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">22.04</td>
    <td align="right">20.73</td>
    <td align="right">25.02</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">25.77</td>
    <td align="right">26.56</td>
    <td align="right">29.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">90.63</td>
    <td align="right">86.22</td>
    <td align="right">46.50</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.99</td>
    <td align="right">21.93</td>
    <td align="right">24.66</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">27.13</td>
    <td align="right">28.69</td>
    <td align="right">31.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">111.84</td>
    <td align="right">103.82</td>
    <td align="right">45.79</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.43</td>
    <td align="right">22.87</td>
    <td align="right">24.32</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.77</td>
    <td align="right">30.80</td>
    <td align="right">32.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">140.58</td>
    <td align="right">123.58</td>
    <td align="right">44.06</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.69</td>
    <td align="right">24.41</td>
    <td align="right">25.24</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">31.30</td>
    <td align="right">34.08</td>
    <td align="right">33.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1768</td>
    <td align="right">90.92</td>
    <td align="right">83.30</td>
    <td align="right">54.64</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">26.98</td>
    <td align="right">26.13</td>
    <td align="right">29.65</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">30.43</td>
    <td align="right">29.87</td>
    <td align="right">32.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">140.68</td>
    <td align="right">122.60</td>
    <td align="right">56.16</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">29.40</td>
    <td align="right">27.27</td>
    <td align="right">29.47</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">32.65</td>
    <td align="right">31.96</td>
    <td align="right">33.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">171.76</td>
    <td align="right">147.91</td>
    <td align="right">54.87</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">30.53</td>
    <td align="right">27.95</td>
    <td align="right">29.40</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">35.16</td>
    <td align="right">34.68</td>
    <td align="right">36.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">220.00</td>
    <td align="right">186.92</td>
    <td align="right">55.35</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">33.39</td>
    <td align="right">29.50</td>
    <td align="right">30.40</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">36.66</td>
    <td align="right">36.46</td>
    <td align="right">37.89</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">23.51</td>
    <td align="right">45.90</td>
    <td align="right">45.66</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.08</td>
    <td align="right">46.07</td>
    <td align="right">46.37</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.82</td>
    <td align="right">25.52</td>
    <td align="right">25.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.29</td>
    <td align="right">61.05</td>
    <td align="right">61.51</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.92</td>
    <td align="right">61.88</td>
    <td align="right">62.27</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.67</td>
    <td align="right">36.65</td>
    <td align="right">25.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.75</td>
    <td align="right">81.23</td>
    <td align="right">83.50</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">45.39</td>
    <td align="right">83.14</td>
    <td align="right">81.83</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.16</td>
    <td align="right">55.33</td>
    <td align="right">39.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">44.22</td>
    <td align="right">92.62</td>
    <td align="right">92.02</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">51.40</td>
    <td align="right">97.62</td>
    <td align="right">98.51</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.50</td>
    <td align="right">55.97</td>
    <td align="right">40.33</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">28.59</td>
    <td align="right">46.71</td>
    <td align="right">47.37</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">32.81</td>
    <td align="right">47.72</td>
    <td align="right">48.31</td>
    <td align="center">5</td>
    <td align="right">2.7313</td>
    <td align="right">22.71</td>
    <td align="right">26.83</td>
    <td align="right">26.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">32.69</td>
    <td align="right">62.62</td>
    <td align="right">63.10</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">39.94</td>
    <td align="right">63.72</td>
    <td align="right">65.29</td>
    <td align="center">8</td>
    <td align="right">0.5366</td>
    <td align="right">22.60</td>
    <td align="right">38.53</td>
    <td align="right">26.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">45.07</td>
    <td align="right">85.06</td>
    <td align="right">85.75</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">51.69</td>
    <td align="right">85.97</td>
    <td align="right">87.38</td>
    <td align="center">11</td>
    <td align="right">0.1134</td>
    <td align="right">31.78</td>
    <td align="right">56.20</td>
    <td align="right">39.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">48.95</td>
    <td align="right">97.45</td>
    <td align="right">97.12</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">57.68</td>
    <td align="right">100.02</td>
    <td align="right">101.06</td>
    <td align="center">13</td>
    <td align="right">0.0253</td>
    <td align="right">32.02</td>
    <td align="right">56.99</td>
    <td align="right">40.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">18.74</td>
    <td align="right">26.45</td>
    <td align="right">26.48</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.73</td>
    <td align="right">29.47</td>
    <td align="right">29.56</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">21.00</td>
    <td align="right">31.56</td>
    <td align="right">31.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">19.16</td>
    <td align="right">46.92</td>
    <td align="right">34.88</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.57</td>
    <td align="right">40.35</td>
    <td align="right">27.93</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.10</td>
    <td align="right">52.56</td>
    <td align="right">40.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.79</td>
    <td align="right">55.06</td>
    <td align="right">39.05</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.29</td>
    <td align="right">53.27</td>
    <td align="right">35.86</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.53</td>
    <td align="right">61.95</td>
    <td align="right">44.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">29.17</td>
    <td align="right">55.65</td>
    <td align="right">39.83</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.69</td>
    <td align="right">66.09</td>
    <td align="right">44.99</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.39</td>
    <td align="right">64.07</td>
    <td align="right">44.96</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4533</td>
    <td align="right">22.69</td>
    <td align="right">27.73</td>
    <td align="right">27.47</td>
    <td align="center">5</td>
    <td align="right">2.4471</td>
    <td align="right">23.98</td>
    <td align="right">29.44</td>
    <td align="right">29.38</td>
    <td align="center">5</td>
    <td align="right">2.3272</td>
    <td align="right">24.16</td>
    <td align="right">30.57</td>
    <td align="right">30.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4375</td>
    <td align="right">23.52</td>
    <td align="right">47.77</td>
    <td align="right">35.83</td>
    <td align="center">8</td>
    <td align="right">0.4137</td>
    <td align="right">23.39</td>
    <td align="right">40.20</td>
    <td align="right">27.82</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">25.49</td>
    <td align="right">54.41</td>
    <td align="right">40.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0906</td>
    <td align="right">31.11</td>
    <td align="right">55.72</td>
    <td align="right">39.94</td>
    <td align="center">11</td>
    <td align="right">0.0740</td>
    <td align="right">34.92</td>
    <td align="right">62.41</td>
    <td align="right">44.48</td>
    <td align="center">11</td>
    <td align="right">0.0604</td>
    <td align="right">34.71</td>
    <td align="right">62.35</td>
    <td align="right">44.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">31.33</td>
    <td align="right">56.29</td>
    <td align="right">40.50</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">35.51</td>
    <td align="right">66.52</td>
    <td align="right">45.72</td>
    <td align="center">14</td>
    <td align="right">0.0129</td>
    <td align="right">35.25</td>
    <td align="right">66.01</td>
    <td align="right">45.18</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">67.79</td>
    <td align="right">36.54</td>
    <td align="right">12.63</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">68.32</td>
    <td align="right">60.47</td>
    <td align="right">47.33</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">30.01</td>
    <td align="right">24.07</td>
    <td align="right">27.89</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">28.97</td>
    <td align="right">30.15</td>
    <td align="right">33.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">111.32</td>
    <td align="right">100.02</td>
    <td align="right">52.89</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">32.51</td>
    <td align="right">28.14</td>
    <td align="right">31.23</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">37.40</td>
    <td align="right">38.23</td>
    <td align="right">39.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">196.78</td>
    <td align="right">173.52</td>
    <td align="right">70.99</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">42.70</td>
    <td align="right">34.62</td>
    <td align="right">37.12</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">52.11</td>
    <td align="right">54.95</td>
    <td align="right">50.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">332.95</td>
    <td align="right">258.21</td>
    <td align="right">68.78</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">56.57</td>
    <td align="right">42.46</td>
    <td align="right">42.71</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">62.40</td>
    <td align="right">64.55</td>
    <td align="right">60.47</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1542</td>
    <td align="right">107.85</td>
    <td align="right">95.16</td>
    <td align="right">60.01</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">30.10</td>
    <td align="right">27.33</td>
    <td align="right">32.46</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">34.92</td>
    <td align="right">34.13</td>
    <td align="right">37.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">174.76</td>
    <td align="right">139.23</td>
    <td align="right">61.54</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">35.63</td>
    <td align="right">30.15</td>
    <td align="right">34.19</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">41.27</td>
    <td align="right">39.38</td>
    <td align="right">44.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">257.62</td>
    <td align="right">201.01</td>
    <td align="right">68.29</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">44.66</td>
    <td align="right">38.63</td>
    <td align="right">38.89</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">51.48</td>
    <td align="right">53.84</td>
    <td align="right">52.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">441.19</td>
    <td align="right">340.52</td>
    <td align="right">80.87</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">60.59</td>
    <td align="right">47.05</td>
    <td align="right">47.13</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">64.89</td>
    <td align="right">66.26</td>
    <td align="right">66.27</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">25.96</td>
    <td align="right">49.77</td>
    <td align="right">49.55</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">32.73</td>
    <td align="right">48.68</td>
    <td align="right">48.38</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">20.45</td>
    <td align="right">30.97</td>
    <td align="right">31.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">34.52</td>
    <td align="right">69.33</td>
    <td align="right">69.60</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">44.88</td>
    <td align="right">78.30</td>
    <td align="right">80.44</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">26.88</td>
    <td align="right">50.83</td>
    <td align="right">35.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">53.69</td>
    <td align="right">101.04</td>
    <td align="right">104.72</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">59.46</td>
    <td align="right">98.01</td>
    <td align="right">96.56</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">54.87</td>
    <td align="right">90.50</td>
    <td align="right">71.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">61.98</td>
    <td align="right">109.71</td>
    <td align="right">108.93</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">75.90</td>
    <td align="right">123.46</td>
    <td align="right">125.15</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">66.31</td>
    <td align="right">106.62</td>
    <td align="right">83.98</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">33.01</td>
    <td align="right">49.96</td>
    <td align="right">49.28</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">39.25</td>
    <td align="right">52.56</td>
    <td align="right">52.71</td>
    <td align="center">5</td>
    <td align="right">2.7250</td>
    <td align="right">26.23</td>
    <td align="right">30.94</td>
    <td align="right">30.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">39.86</td>
    <td align="right">71.59</td>
    <td align="right">73.77</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">51.00</td>
    <td align="right">76.42</td>
    <td align="right">78.18</td>
    <td align="center">8</td>
    <td align="right">0.5385</td>
    <td align="right">26.33</td>
    <td align="right">47.31</td>
    <td align="right">32.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">57.88</td>
    <td align="right">95.07</td>
    <td align="right">96.13</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">63.61</td>
    <td align="right">96.81</td>
    <td align="right">98.11</td>
    <td align="center">11</td>
    <td align="right">0.1183</td>
    <td align="right">54.32</td>
    <td align="right">88.09</td>
    <td align="right">65.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">69.72</td>
    <td align="right">116.46</td>
    <td align="right">114.92</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">83.83</td>
    <td align="right">122.71</td>
    <td align="right">124.23</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">65.21</td>
    <td align="right">101.66</td>
    <td align="right">80.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">20.84</td>
    <td align="right">31.76</td>
    <td align="right">31.97</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">22.45</td>
    <td align="right">34.80</td>
    <td align="right">34.75</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">22.45</td>
    <td align="right">38.38</td>
    <td align="right">37.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">21.86</td>
    <td align="right">58.69</td>
    <td align="right">44.73</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">20.88</td>
    <td align="right">57.09</td>
    <td align="right">36.94</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">24.29</td>
    <td align="right">68.70</td>
    <td align="right">51.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">48.61</td>
    <td align="right">85.37</td>
    <td align="right">66.13</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">44.45</td>
    <td align="right">73.72</td>
    <td align="right">63.07</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">45.96</td>
    <td align="right">80.39</td>
    <td align="right">57.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">63.51</td>
    <td align="right">101.95</td>
    <td align="right">87.34</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">54.69</td>
    <td align="right">100.95</td>
    <td align="right">77.05</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">47.68</td>
    <td align="right">92.14</td>
    <td align="right">67.18</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4644</td>
    <td align="right">25.62</td>
    <td align="right">32.50</td>
    <td align="right">32.78</td>
    <td align="center">5</td>
    <td align="right">2.4405</td>
    <td align="right">27.82</td>
    <td align="right">36.81</td>
    <td align="right">36.85</td>
    <td align="center">5</td>
    <td align="right">2.3265</td>
    <td align="right">27.18</td>
    <td align="right">35.59</td>
    <td align="right">35.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4413</td>
    <td align="right">29.60</td>
    <td align="right">64.04</td>
    <td align="right">47.19</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">33.31</td>
    <td align="right">47.17</td>
    <td align="right">35.29</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">34.40</td>
    <td align="right">73.42</td>
    <td align="right">52.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0845</td>
    <td align="right">64.62</td>
    <td align="right">110.30</td>
    <td align="right">105.15</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">50.80</td>
    <td align="right">100.91</td>
    <td align="right">72.55</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">52.91</td>
    <td align="right">92.48</td>
    <td align="right">67.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">81.34</td>
    <td align="right">121.18</td>
    <td align="right">106.67</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">68.19</td>
    <td align="right">100.50</td>
    <td align="right">85.85</td>
    <td align="center">14</td>
    <td align="right">0.0116</td>
    <td align="right">73.76</td>
    <td align="right">114.02</td>
    <td align="right">79.44</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
