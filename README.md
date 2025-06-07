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
    <td align="right">26.91</td>
    <td align="right">5.27</td>
    <td align="right">4.03</td>
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
    <td align="right">10.64</td>
    <td align="right">10.51</td>
    <td align="right">15.94</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.81</td>
    <td align="right">4.11</td>
    <td align="right">4.10</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.67</td>
    <td align="right">4.86</td>
    <td align="right">4.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">15.95</td>
    <td align="right">14.44</td>
    <td align="right">16.79</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.51</td>
    <td align="right">4.64</td>
    <td align="right">4.66</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.13</td>
    <td align="right">5.18</td>
    <td align="right">5.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">18.77</td>
    <td align="right">17.46</td>
    <td align="right">15.85</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.09</td>
    <td align="right">5.01</td>
    <td align="right">5.10</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.90</td>
    <td align="right">5.96</td>
    <td align="right">5.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">24.46</td>
    <td align="right">21.21</td>
    <td align="right">16.19</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.06</td>
    <td align="right">5.70</td>
    <td align="right">5.51</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.33</td>
    <td align="right">6.19</td>
    <td align="right">6.17</td>
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
    <td align="right">10.15</td>
    <td align="right">10.49</td>
    <td align="right">16.18</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">3.77</td>
    <td align="right">4.13</td>
    <td align="right">4.09</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">4.44</td>
    <td align="right">4.97</td>
    <td align="right">5.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">14.90</td>
    <td align="right">14.92</td>
    <td align="right">17.16</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">4.26</td>
    <td align="right">4.95</td>
    <td align="right">5.00</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">5.12</td>
    <td align="right">5.54</td>
    <td align="right">5.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">17.97</td>
    <td align="right">18.15</td>
    <td align="right">16.54</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">4.76</td>
    <td align="right">5.33</td>
    <td align="right">5.28</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">5.52</td>
    <td align="right">6.17</td>
    <td align="right">6.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">21.92</td>
    <td align="right">22.00</td>
    <td align="right">16.49</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">5.13</td>
    <td align="right">5.95</td>
    <td align="right">5.94</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">5.94</td>
    <td align="right">6.51</td>
    <td align="right">6.60</td>
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
    <td align="right">4.88</td>
    <td align="right">5.08</td>
    <td align="right">5.08</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.29</td>
    <td align="right">5.97</td>
    <td align="right">6.21</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.86</td>
    <td align="right">3.15</td>
    <td align="right">3.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.64</td>
    <td align="right">7.76</td>
    <td align="right">7.76</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.77</td>
    <td align="right">9.27</td>
    <td align="right">9.35</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.39</td>
    <td align="right">2.98</td>
    <td align="right">2.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">8.90</td>
    <td align="right">12.08</td>
    <td align="right">12.13</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.74</td>
    <td align="right">12.87</td>
    <td align="right">12.89</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.51</td>
    <td align="right">5.52</td>
    <td align="right">3.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">10.48</td>
    <td align="right">13.79</td>
    <td align="right">13.80</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">11.37</td>
    <td align="right">15.84</td>
    <td align="right">15.80</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.62</td>
    <td align="right">5.55</td>
    <td align="right">3.68</td>
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
    <td align="right">4.59</td>
    <td align="right">5.22</td>
    <td align="right">5.24</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">5.46</td>
    <td align="right">6.03</td>
    <td align="right">6.05</td>
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
    <td align="right">5.88</td>
    <td align="right">7.93</td>
    <td align="right">7.93</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">7.10</td>
    <td align="right">9.28</td>
    <td align="right">9.26</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.38</td>
    <td align="right">2.57</td>
    <td align="right">2.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">8.80</td>
    <td align="right">11.39</td>
    <td align="right">11.55</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">16.98</td>
    <td align="right">13.51</td>
    <td align="right">13.66</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">5.48</td>
    <td align="right">5.68</td>
    <td align="right">3.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">10.82</td>
    <td align="right">13.54</td>
    <td align="right">13.48</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">11.90</td>
    <td align="right">15.97</td>
    <td align="right">16.08</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">5.53</td>
    <td align="right">5.73</td>
    <td align="right">3.87</td>
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
    <td align="right">2.80</td>
    <td align="right">4.01</td>
    <td align="right">3.05</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.25</td>
    <td align="right">4.86</td>
    <td align="right">4.81</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.36</td>
    <td align="right">4.68</td>
    <td align="right">4.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.91</td>
    <td align="right">3.11</td>
    <td align="right">3.10</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.96</td>
    <td align="right">4.23</td>
    <td align="right">4.24</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.22</td>
    <td align="right">4.79</td>
    <td align="right">4.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.21</td>
    <td align="right">5.17</td>
    <td align="right">3.55</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">6.61</td>
    <td align="right">7.30</td>
    <td align="right">5.53</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.44</td>
    <td align="right">7.09</td>
    <td align="right">5.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.25</td>
    <td align="right">5.15</td>
    <td align="right">3.53</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">7.69</td>
    <td align="right">8.66</td>
    <td align="right">5.77</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.06</td>
    <td align="right">8.51</td>
    <td align="right">5.59</td>
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
    <td align="right">2.93</td>
    <td align="right">2.66</td>
    <td align="right">2.61</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">4.35</td>
    <td align="right">4.51</td>
    <td align="right">4.56</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">4.38</td>
    <td align="right">4.45</td>
    <td align="right">4.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.03</td>
    <td align="right">2.69</td>
    <td align="right">2.69</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">3.05</td>
    <td align="right">3.83</td>
    <td align="right">3.83</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">4.33</td>
    <td align="right">4.52</td>
    <td align="right">4.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">5.12</td>
    <td align="right">5.34</td>
    <td align="right">3.61</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">7.08</td>
    <td align="right">7.51</td>
    <td align="right">5.78</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">7.49</td>
    <td align="right">7.18</td>
    <td align="right">5.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">5.17</td>
    <td align="right">5.39</td>
    <td align="right">3.59</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">7.71</td>
    <td align="right">8.81</td>
    <td align="right">5.80</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">8.02</td>
    <td align="right">8.53</td>
    <td align="right">5.52</td>
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
    <td align="right">29.99</td>
    <td align="right">17.88</td>
    <td align="right">6.48</td>
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
    <td align="right">13.78</td>
    <td align="right">12.98</td>
    <td align="right">17.72</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.72</td>
    <td align="right">5.08</td>
    <td align="right">5.03</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.76</td>
    <td align="right">5.92</td>
    <td align="right">5.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.32</td>
    <td align="right">18.08</td>
    <td align="right">18.04</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.33</td>
    <td align="right">5.50</td>
    <td align="right">5.71</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.01</td>
    <td align="right">6.05</td>
    <td align="right">6.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">25.18</td>
    <td align="right">23.52</td>
    <td align="right">17.84</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.42</td>
    <td align="right">6.27</td>
    <td align="right">6.17</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.52</td>
    <td align="right">7.61</td>
    <td align="right">7.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">43.88</td>
    <td align="right">39.15</td>
    <td align="right">18.32</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.95</td>
    <td align="right">9.86</td>
    <td align="right">8.17</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.90</td>
    <td align="right">8.84</td>
    <td align="right">10.09</td>
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
    <td align="right">12.97</td>
    <td align="right">13.44</td>
    <td align="right">18.04</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">4.49</td>
    <td align="right">5.05</td>
    <td align="right">5.05</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">5.57</td>
    <td align="right">6.14</td>
    <td align="right">6.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">18.74</td>
    <td align="right">19.31</td>
    <td align="right">18.41</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">5.04</td>
    <td align="right">5.73</td>
    <td align="right">5.75</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">6.24</td>
    <td align="right">6.23</td>
    <td align="right">6.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">27.82</td>
    <td align="right">24.70</td>
    <td align="right">18.59</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">10.50</td>
    <td align="right">8.87</td>
    <td align="right">7.19</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">6.85</td>
    <td align="right">8.22</td>
    <td align="right">7.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">41.56</td>
    <td align="right">40.78</td>
    <td align="right">18.86</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">7.72</td>
    <td align="right">8.87</td>
    <td align="right">8.36</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.31</td>
    <td align="right">9.44</td>
    <td align="right">10.11</td>
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
    <td align="right">5.98</td>
    <td align="right">6.77</td>
    <td align="right">6.76</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.46</td>
    <td align="right">7.92</td>
    <td align="right">8.17</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.53</td>
    <td align="right">4.02</td>
    <td align="right">4.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.78</td>
    <td align="right">9.70</td>
    <td align="right">9.81</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.97</td>
    <td align="right">10.83</td>
    <td align="right">10.93</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.74</td>
    <td align="right">3.39</td>
    <td align="right">3.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.80</td>
    <td align="right">15.14</td>
    <td align="right">14.91</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.54</td>
    <td align="right">15.97</td>
    <td align="right">15.45</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.18</td>
    <td align="right">6.90</td>
    <td align="right">5.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">13.84</td>
    <td align="right">18.39</td>
    <td align="right">17.86</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.06</td>
    <td align="right">22.24</td>
    <td align="right">20.34</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">8.18</td>
    <td align="right">9.04</td>
    <td align="right">5.27</td>
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
    <td align="right">5.65</td>
    <td align="right">6.98</td>
    <td align="right">6.97</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">6.69</td>
    <td align="right">7.98</td>
    <td align="right">8.00</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.63</td>
    <td align="right">3.55</td>
    <td align="right">3.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">6.77</td>
    <td align="right">9.71</td>
    <td align="right">9.81</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">8.09</td>
    <td align="right">10.87</td>
    <td align="right">10.96</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">2.88</td>
    <td align="right">3.06</td>
    <td align="right">3.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">10.57</td>
    <td align="right">14.19</td>
    <td align="right">14.38</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">17.68</td>
    <td align="right">17.85</td>
    <td align="right">16.76</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">6.85</td>
    <td align="right">7.00</td>
    <td align="right">5.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">13.88</td>
    <td align="right">16.95</td>
    <td align="right">18.48</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">16.45</td>
    <td align="right">23.90</td>
    <td align="right">20.21</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">8.63</td>
    <td align="right">8.70</td>
    <td align="right">7.28</td>
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
    <td align="right">3.51</td>
    <td align="right">3.94</td>
    <td align="right">3.94</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.13</td>
    <td align="right">6.02</td>
    <td align="right">5.93</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.26</td>
    <td align="right">5.88</td>
    <td align="right">5.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.45</td>
    <td align="right">3.82</td>
    <td align="right">3.83</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.59</td>
    <td align="right">5.21</td>
    <td align="right">5.04</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.98</td>
    <td align="right">5.88</td>
    <td align="right">6.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.30</td>
    <td align="right">7.52</td>
    <td align="right">5.79</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.39</td>
    <td align="right">11.66</td>
    <td align="right">8.14</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.53</td>
    <td align="right">9.87</td>
    <td align="right">9.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">8.01</td>
    <td align="right">8.74</td>
    <td align="right">6.08</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">10.42</td>
    <td align="right">11.42</td>
    <td align="right">8.64</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">10.30</td>
    <td align="right">12.47</td>
    <td align="right">8.26</td>
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
    <td align="right">3.54</td>
    <td align="right">3.18</td>
    <td align="right">3.20</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">5.26</td>
    <td align="right">5.58</td>
    <td align="right">5.55</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">5.30</td>
    <td align="right">5.43</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.59</td>
    <td align="right">3.32</td>
    <td align="right">3.35</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">3.66</td>
    <td align="right">4.46</td>
    <td align="right">4.64</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">5.11</td>
    <td align="right">5.36</td>
    <td align="right">5.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">5.93</td>
    <td align="right">6.62</td>
    <td align="right">4.53</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">9.40</td>
    <td align="right">9.56</td>
    <td align="right">7.43</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">8.93</td>
    <td align="right">8.99</td>
    <td align="right">7.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">7.11</td>
    <td align="right">8.18</td>
    <td align="right">5.64</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">10.72</td>
    <td align="right">11.75</td>
    <td align="right">8.12</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">10.52</td>
    <td align="right">12.73</td>
    <td align="right">8.22</td>
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
    <td align="right">26.18</td>
    <td align="right">4.02</td>
    <td align="right">3.36</td>
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
    <td align="right">9.13</td>
    <td align="right">8.86</td>
    <td align="right">15.49</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.41</td>
    <td align="right">3.94</td>
    <td align="right">3.93</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.84</td>
    <td align="right">4.54</td>
    <td align="right">4.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.02</td>
    <td align="right">14.16</td>
    <td align="right">16.72</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.83</td>
    <td align="right">4.54</td>
    <td align="right">4.56</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.47</td>
    <td align="right">5.26</td>
    <td align="right">5.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.15</td>
    <td align="right">16.34</td>
    <td align="right">15.52</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.32</td>
    <td align="right">5.06</td>
    <td align="right">5.06</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.92</td>
    <td align="right">5.97</td>
    <td align="right">5.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.66</td>
    <td align="right">20.79</td>
    <td align="right">16.09</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.80</td>
    <td align="right">5.84</td>
    <td align="right">5.84</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.81</td>
    <td align="right">3.27</td>
    <td align="right">3.26</td>
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
    <td align="right">10.29</td>
    <td align="right">10.01</td>
    <td align="right">16.37</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">4.20</td>
    <td align="right">4.22</td>
    <td align="right">4.11</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">3.99</td>
    <td align="right">4.86</td>
    <td align="right">4.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">15.24</td>
    <td align="right">15.22</td>
    <td align="right">17.50</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">4.64</td>
    <td align="right">4.71</td>
    <td align="right">4.69</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">4.62</td>
    <td align="right">5.63</td>
    <td align="right">5.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">18.38</td>
    <td align="right">17.75</td>
    <td align="right">16.40</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">5.13</td>
    <td align="right">5.24</td>
    <td align="right">5.23</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">5.16</td>
    <td align="right">6.06</td>
    <td align="right">6.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">23.30</td>
    <td align="right">22.28</td>
    <td align="right">16.70</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">5.61</td>
    <td align="right">6.11</td>
    <td align="right">5.91</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">3.15</td>
    <td align="right">3.46</td>
    <td align="right">3.46</td>
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
    <td align="right">3.03</td>
    <td align="right">3.55</td>
    <td align="right">3.55</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.13</td>
    <td align="right">3.46</td>
    <td align="right">3.46</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.55</td>
    <td align="right">2.48</td>
    <td align="right">2.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.69</td>
    <td align="right">3.34</td>
    <td align="right">3.35</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.70</td>
    <td align="right">3.67</td>
    <td align="right">3.68</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.12</td>
    <td align="right">2.24</td>
    <td align="right">2.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.49</td>
    <td align="right">6.11</td>
    <td align="right">6.10</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.69</td>
    <td align="right">6.03</td>
    <td align="right">6.02</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.13</td>
    <td align="right">4.33</td>
    <td align="right">3.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.94</td>
    <td align="right">6.61</td>
    <td align="right">6.50</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.23</td>
    <td align="right">6.91</td>
    <td align="right">7.16</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.18</td>
    <td align="right">4.35</td>
    <td align="right">3.09</td>
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
    <td align="right">3.16</td>
    <td align="right">3.74</td>
    <td align="right">3.75</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">3.30</td>
    <td align="right">3.64</td>
    <td align="right">3.69</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">2.87</td>
    <td align="right">2.74</td>
    <td align="right">2.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">3.36</td>
    <td align="right">3.67</td>
    <td align="right">3.66</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">3.86</td>
    <td align="right">3.96</td>
    <td align="right">3.97</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.77</td>
    <td align="right">2.57</td>
    <td align="right">2.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">5.76</td>
    <td align="right">6.47</td>
    <td align="right">6.44</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">5.84</td>
    <td align="right">6.61</td>
    <td align="right">6.61</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">4.45</td>
    <td align="right">4.66</td>
    <td align="right">3.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">6.15</td>
    <td align="right">6.63</td>
    <td align="right">6.81</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">6.50</td>
    <td align="right">7.10</td>
    <td align="right">7.12</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">4.48</td>
    <td align="right">4.72</td>
    <td align="right">3.40</td>
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
    <td align="right">2.57</td>
    <td align="right">2.30</td>
    <td align="right">2.30</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.61</td>
    <td align="right">4.03</td>
    <td align="right">4.02</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.66</td>
    <td align="right">3.88</td>
    <td align="right">3.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.66</td>
    <td align="right">2.39</td>
    <td align="right">2.36</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.91</td>
    <td align="right">3.69</td>
    <td align="right">3.70</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.82</td>
    <td align="right">4.00</td>
    <td align="right">3.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.20</td>
    <td align="right">4.24</td>
    <td align="right">2.88</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.59</td>
    <td align="right">5.98</td>
    <td align="right">4.63</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.75</td>
    <td align="right">5.95</td>
    <td align="right">4.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.24</td>
    <td align="right">4.29</td>
    <td align="right">2.87</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.53</td>
    <td align="right">7.06</td>
    <td align="right">4.61</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.74</td>
    <td align="right">6.97</td>
    <td align="right">4.53</td>
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
    <td align="right">2.78</td>
    <td align="right">2.64</td>
    <td align="right">2.64</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">3.78</td>
    <td align="right">4.31</td>
    <td align="right">4.31</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">3.87</td>
    <td align="right">4.26</td>
    <td align="right">4.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">2.93</td>
    <td align="right">2.71</td>
    <td align="right">2.71</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">3.59</td>
    <td align="right">3.99</td>
    <td align="right">3.99</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">4.08</td>
    <td align="right">4.30</td>
    <td align="right">4.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">4.44</td>
    <td align="right">4.56</td>
    <td align="right">3.16</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">5.82</td>
    <td align="right">6.38</td>
    <td align="right">4.82</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">5.91</td>
    <td align="right">6.24</td>
    <td align="right">4.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">4.43</td>
    <td align="right">4.58</td>
    <td align="right">3.15</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">6.97</td>
    <td align="right">7.41</td>
    <td align="right">4.89</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">6.96</td>
    <td align="right">7.29</td>
    <td align="right">4.81</td>
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
    <td align="right">31.01</td>
    <td align="right">16.89</td>
    <td align="right">5.85</td>
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
    <td align="right">10.81</td>
    <td align="right">10.42</td>
    <td align="right">16.12</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.83</td>
    <td align="right">4.47</td>
    <td align="right">4.47</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.36</td>
    <td align="right">5.07</td>
    <td align="right">5.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">14.45</td>
    <td align="right">14.98</td>
    <td align="right">17.04</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.17</td>
    <td align="right">4.86</td>
    <td align="right">4.85</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">4.94</td>
    <td align="right">5.71</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">18.66</td>
    <td align="right">18.42</td>
    <td align="right">16.20</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.03</td>
    <td align="right">5.68</td>
    <td align="right">5.67</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">5.58</td>
    <td align="right">6.61</td>
    <td align="right">6.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">26.74</td>
    <td align="right">26.59</td>
    <td align="right">16.84</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">5.91</td>
    <td align="right">6.78</td>
    <td align="right">6.70</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">4.00</td>
    <td align="right">4.31</td>
    <td align="right">4.31</td>
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
    <td align="right">11.76</td>
    <td align="right">11.77</td>
    <td align="right">17.30</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">4.86</td>
    <td align="right">4.79</td>
    <td align="right">4.68</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">4.65</td>
    <td align="right">5.46</td>
    <td align="right">5.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">16.79</td>
    <td align="right">16.78</td>
    <td align="right">17.90</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">5.07</td>
    <td align="right">5.08</td>
    <td align="right">5.06</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">5.05</td>
    <td align="right">6.03</td>
    <td align="right">5.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">21.05</td>
    <td align="right">21.61</td>
    <td align="right">17.08</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">5.94</td>
    <td align="right">5.92</td>
    <td align="right">5.90</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">5.79</td>
    <td align="right">6.80</td>
    <td align="right">6.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">30.11</td>
    <td align="right">30.05</td>
    <td align="right">17.44</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">6.88</td>
    <td align="right">7.10</td>
    <td align="right">7.03</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">4.20</td>
    <td align="right">4.59</td>
    <td align="right">4.53</td>
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
    <td align="right">3.57</td>
    <td align="right">4.17</td>
    <td align="right">4.18</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.66</td>
    <td align="right">4.09</td>
    <td align="right">4.10</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.01</td>
    <td align="right">3.00</td>
    <td align="right">3.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.02</td>
    <td align="right">3.69</td>
    <td align="right">3.73</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.00</td>
    <td align="right">4.14</td>
    <td align="right">4.14</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.39</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">6.57</td>
    <td align="right">7.17</td>
    <td align="right">7.13</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">6.65</td>
    <td align="right">7.27</td>
    <td align="right">7.27</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">4.66</td>
    <td align="right">5.03</td>
    <td align="right">3.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">7.31</td>
    <td align="right">8.28</td>
    <td align="right">8.18</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">7.53</td>
    <td align="right">8.80</td>
    <td align="right">8.87</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">5.27</td>
    <td align="right">5.67</td>
    <td align="right">4.19</td>
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
    <td align="right">3.72</td>
    <td align="right">4.37</td>
    <td align="right">4.37</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">3.82</td>
    <td align="right">4.27</td>
    <td align="right">4.33</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.33</td>
    <td align="right">3.26</td>
    <td align="right">3.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">3.72</td>
    <td align="right">4.00</td>
    <td align="right">4.01</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">4.16</td>
    <td align="right">4.40</td>
    <td align="right">4.43</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">3.12</td>
    <td align="right">2.90</td>
    <td align="right">2.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">6.83</td>
    <td align="right">7.74</td>
    <td align="right">7.71</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">6.84</td>
    <td align="right">8.04</td>
    <td align="right">7.94</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">5.03</td>
    <td align="right">5.47</td>
    <td align="right">4.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">7.63</td>
    <td align="right">8.50</td>
    <td align="right">8.56</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">8.13</td>
    <td align="right">9.23</td>
    <td align="right">9.13</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">5.79</td>
    <td align="right">6.23</td>
    <td align="right">4.57</td>
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
    <td align="right">3.01</td>
    <td align="right">2.84</td>
    <td align="right">2.86</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.19</td>
    <td align="right">4.71</td>
    <td align="right">4.72</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.23</td>
    <td align="right">4.60</td>
    <td align="right">4.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.94</td>
    <td align="right">2.81</td>
    <td align="right">2.82</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.27</td>
    <td align="right">4.10</td>
    <td align="right">4.09</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.14</td>
    <td align="right">4.45</td>
    <td align="right">4.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">4.73</td>
    <td align="right">5.01</td>
    <td align="right">3.58</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">6.62</td>
    <td align="right">7.38</td>
    <td align="right">5.85</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">6.77</td>
    <td align="right">7.21</td>
    <td align="right">5.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">5.71</td>
    <td align="right">6.09</td>
    <td align="right">4.34</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">7.98</td>
    <td align="right">8.78</td>
    <td align="right">6.05</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">8.54</td>
    <td align="right">9.24</td>
    <td align="right">6.20</td>
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
    <td align="right">3.26</td>
    <td align="right">3.20</td>
    <td align="right">3.21</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">4.45</td>
    <td align="right">4.55</td>
    <td align="right">4.29</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">4.51</td>
    <td align="right">5.00</td>
    <td align="right">4.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.24</td>
    <td align="right">3.13</td>
    <td align="right">3.14</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">4.00</td>
    <td align="right">4.43</td>
    <td align="right">4.42</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">4.45</td>
    <td align="right">4.82</td>
    <td align="right">4.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">5.05</td>
    <td align="right">5.39</td>
    <td align="right">3.66</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">6.97</td>
    <td align="right">7.96</td>
    <td align="right">6.23</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">6.99</td>
    <td align="right">7.79</td>
    <td align="right">6.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">5.85</td>
    <td align="right">6.28</td>
    <td align="right">4.57</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">8.49</td>
    <td align="right">9.34</td>
    <td align="right">6.53</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">8.87</td>
    <td align="right">9.49</td>
    <td align="right">6.66</td>
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
    <td align="right">21.79</td>
    <td align="right">3.62</td>
    <td align="right">3.56</td>
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
    <td align="right">6.63</td>
    <td align="right">5.38</td>
    <td align="right">12.46</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.41</td>
    <td align="right">1.28</td>
    <td align="right">1.30</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.71</td>
    <td align="right">1.45</td>
    <td align="right">1.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.05</td>
    <td align="right">7.64</td>
    <td align="right">13.06</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.53</td>
    <td align="right">1.51</td>
    <td align="right">1.48</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.82</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">14.85</td>
    <td align="right">9.48</td>
    <td align="right">12.20</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.78</td>
    <td align="right">1.72</td>
    <td align="right">1.68</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.04</td>
    <td align="right">1.78</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.93</td>
    <td align="right">12.55</td>
    <td align="right">12.22</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.79</td>
    <td align="right">2.09</td>
    <td align="right">2.21</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.90</td>
    <td align="right">1.68</td>
    <td align="right">1.74</td>
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
    <td align="right">7.49</td>
    <td align="right">4.71</td>
    <td align="right">12.69</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">1.52</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">1.75</td>
    <td align="right">1.45</td>
    <td align="right">1.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">9.66</td>
    <td align="right">6.58</td>
    <td align="right">13.58</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">1.59</td>
    <td align="right">1.64</td>
    <td align="right">1.57</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">1.72</td>
    <td align="right">1.51</td>
    <td align="right">1.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">15.37</td>
    <td align="right">8.15</td>
    <td align="right">11.97</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">1.63</td>
    <td align="right">1.68</td>
    <td align="right">2.07</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">1.89</td>
    <td align="right">1.80</td>
    <td align="right">1.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">19.63</td>
    <td align="right">9.99</td>
    <td align="right">12.68</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">2.15</td>
    <td align="right">2.16</td>
    <td align="right">2.14</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">2.04</td>
    <td align="right">1.77</td>
    <td align="right">1.78</td>
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
    <td align="right">2.47</td>
    <td align="right">1.81</td>
    <td align="right">1.87</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.54</td>
    <td align="right">1.96</td>
    <td align="right">1.96</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.11</td>
    <td align="right">1.90</td>
    <td align="right">1.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.46</td>
    <td align="right">2.74</td>
    <td align="right">2.38</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.12</td>
    <td align="right">2.51</td>
    <td align="right">2.29</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.69</td>
    <td align="right">1.57</td>
    <td align="right">1.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.39</td>
    <td align="right">3.26</td>
    <td align="right">3.26</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.55</td>
    <td align="right">3.26</td>
    <td align="right">3.04</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.18</td>
    <td align="right">2.49</td>
    <td align="right">2.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.11</td>
    <td align="right">4.13</td>
    <td align="right">3.92</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.02</td>
    <td align="right">4.25</td>
    <td align="right">3.86</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.20</td>
    <td align="right">3.41</td>
    <td align="right">1.91</td>
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
    <td align="right">2.29</td>
    <td align="right">1.76</td>
    <td align="right">1.89</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">2.69</td>
    <td align="right">1.93</td>
    <td align="right">1.91</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">2.11</td>
    <td align="right">1.75</td>
    <td align="right">1.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">2.47</td>
    <td align="right">2.19</td>
    <td align="right">2.19</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">3.05</td>
    <td align="right">2.51</td>
    <td align="right">2.44</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">1.68</td>
    <td align="right">1.50</td>
    <td align="right">1.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">4.19</td>
    <td align="right">3.16</td>
    <td align="right">3.08</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">4.21</td>
    <td align="right">3.12</td>
    <td align="right">3.24</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">3.21</td>
    <td align="right">2.68</td>
    <td align="right">1.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">4.67</td>
    <td align="right">4.03</td>
    <td align="right">4.16</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">5.20</td>
    <td align="right">4.01</td>
    <td align="right">3.77</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">3.04</td>
    <td align="right">3.46</td>
    <td align="right">1.98</td>
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
    <td align="right">2.18</td>
    <td align="right">1.87</td>
    <td align="right">1.78</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.47</td>
    <td align="right">1.82</td>
    <td align="right">1.81</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.53</td>
    <td align="right">1.87</td>
    <td align="right">1.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.23</td>
    <td align="right">1.72</td>
    <td align="right">1.67</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.27</td>
    <td align="right">2.96</td>
    <td align="right">2.47</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.12</td>
    <td align="right">2.45</td>
    <td align="right">2.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">2.95</td>
    <td align="right">2.44</td>
    <td align="right">2.14</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.52</td>
    <td align="right">3.15</td>
    <td align="right">3.13</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.46</td>
    <td align="right">3.20</td>
    <td align="right">3.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.21</td>
    <td align="right">3.13</td>
    <td align="right">1.95</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.07</td>
    <td align="right">4.09</td>
    <td align="right">3.99</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.29</td>
    <td align="right">4.27</td>
    <td align="right">4.86</td>
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
    <td align="right">2.06</td>
    <td align="right">1.87</td>
    <td align="right">1.88</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.47</td>
    <td align="right">1.89</td>
    <td align="right">1.85</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">2.49</td>
    <td align="right">1.97</td>
    <td align="right">1.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">2.23</td>
    <td align="right">1.77</td>
    <td align="right">1.73</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">2.68</td>
    <td align="right">2.16</td>
    <td align="right">2.10</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">3.03</td>
    <td align="right">2.45</td>
    <td align="right">2.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">3.21</td>
    <td align="right">2.68</td>
    <td align="right">1.99</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">4.19</td>
    <td align="right">3.19</td>
    <td align="right">3.28</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">4.80</td>
    <td align="right">3.18</td>
    <td align="right">3.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">3.28</td>
    <td align="right">3.50</td>
    <td align="right">1.92</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">5.24</td>
    <td align="right">4.27</td>
    <td align="right">4.03</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">5.09</td>
    <td align="right">4.64</td>
    <td align="right">3.92</td>
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
    <td align="right">30.88</td>
    <td align="right">13.77</td>
    <td align="right">9.42</td>
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
    <td align="right">10.49</td>
    <td align="right">9.91</td>
    <td align="right">18.88</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.10</td>
    <td align="right">4.07</td>
    <td align="right">3.86</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.20</td>
    <td align="right">4.23</td>
    <td align="right">4.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">31.35</td>
    <td align="right">28.56</td>
    <td align="right">24.01</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.55</td>
    <td align="right">6.81</td>
    <td align="right">4.29</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">8.28</td>
    <td align="right">7.31</td>
    <td align="right">7.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">55.10</td>
    <td align="right">41.64</td>
    <td align="right">24.41</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.62</td>
    <td align="right">8.71</td>
    <td align="right">8.89</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.70</td>
    <td align="right">9.54</td>
    <td align="right">10.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">76.42</td>
    <td align="right">55.58</td>
    <td align="right">25.86</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">11.41</td>
    <td align="right">9.20</td>
    <td align="right">8.85</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">11.02</td>
    <td align="right">9.33</td>
    <td align="right">8.61</td>
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
    <td align="right">11.92</td>
    <td align="right">9.89</td>
    <td align="right">19.63</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">4.13</td>
    <td align="right">2.03</td>
    <td align="right">2.53</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">3.42</td>
    <td align="right">3.59</td>
    <td align="right">2.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">35.98</td>
    <td align="right">29.26</td>
    <td align="right">25.39</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">9.10</td>
    <td align="right">6.64</td>
    <td align="right">4.48</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">4.22</td>
    <td align="right">4.33</td>
    <td align="right">5.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">36.84</td>
    <td align="right">27.91</td>
    <td align="right">19.74</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">7.57</td>
    <td align="right">6.86</td>
    <td align="right">6.87</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">7.43</td>
    <td align="right">6.63</td>
    <td align="right">6.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">59.43</td>
    <td align="right">41.23</td>
    <td align="right">21.39</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">9.50</td>
    <td align="right">8.23</td>
    <td align="right">8.35</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">8.05</td>
    <td align="right">6.63</td>
    <td align="right">6.76</td>
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
    <td align="right">2.77</td>
    <td align="right">2.56</td>
    <td align="right">2.57</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.77</td>
    <td align="right">2.64</td>
    <td align="right">2.65</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.50</td>
    <td align="right">2.70</td>
    <td align="right">2.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">5.13</td>
    <td align="right">5.60</td>
    <td align="right">5.56</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">5.54</td>
    <td align="right">6.00</td>
    <td align="right">6.00</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.63</td>
    <td align="right">4.33</td>
    <td align="right">4.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.25</td>
    <td align="right">10.53</td>
    <td align="right">11.36</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">12.27</td>
    <td align="right">10.18</td>
    <td align="right">10.35</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">9.23</td>
    <td align="right">8.71</td>
    <td align="right">6.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.83</td>
    <td align="right">14.75</td>
    <td align="right">14.72</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.84</td>
    <td align="right">14.89</td>
    <td align="right">15.05</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">11.45</td>
    <td align="right">12.13</td>
    <td align="right">7.12</td>
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
    <td align="right">3.08</td>
    <td align="right">2.57</td>
    <td align="right">2.58</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">2.76</td>
    <td align="right">2.62</td>
    <td align="right">2.64</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">2.43</td>
    <td align="right">2.56</td>
    <td align="right">2.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">5.19</td>
    <td align="right">5.57</td>
    <td align="right">5.54</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">6.39</td>
    <td align="right">6.55</td>
    <td align="right">6.05</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">3.74</td>
    <td align="right">4.42</td>
    <td align="right">4.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">12.24</td>
    <td align="right">10.48</td>
    <td align="right">10.53</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">12.30</td>
    <td align="right">10.93</td>
    <td align="right">10.41</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">9.32</td>
    <td align="right">8.71</td>
    <td align="right">6.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">16.29</td>
    <td align="right">14.51</td>
    <td align="right">15.28</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">16.86</td>
    <td align="right">14.80</td>
    <td align="right">14.88</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">10.85</td>
    <td align="right">11.24</td>
    <td align="right">6.83</td>
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
    <td align="right">2.52</td>
    <td align="right">2.56</td>
    <td align="right">2.56</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.75</td>
    <td align="right">2.56</td>
    <td align="right">2.57</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.79</td>
    <td align="right">2.66</td>
    <td align="right">2.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.91</td>
    <td align="right">4.08</td>
    <td align="right">4.06</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">5.10</td>
    <td align="right">6.21</td>
    <td align="right">5.64</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">5.50</td>
    <td align="right">6.11</td>
    <td align="right">7.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">9.15</td>
    <td align="right">8.66</td>
    <td align="right">6.17</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.25</td>
    <td align="right">10.49</td>
    <td align="right">10.48</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">12.25</td>
    <td align="right">11.15</td>
    <td align="right">10.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.99</td>
    <td align="right">11.32</td>
    <td align="right">6.86</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.51</td>
    <td align="right">14.74</td>
    <td align="right">15.30</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">17.40</td>
    <td align="right">14.93</td>
    <td align="right">15.11</td>
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
    <td align="right">2.41</td>
    <td align="right">2.55</td>
    <td align="right">2.56</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">2.76</td>
    <td align="right">2.59</td>
    <td align="right">2.65</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">2.78</td>
    <td align="right">2.86</td>
    <td align="right">3.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.96</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">5.16</td>
    <td align="right">5.54</td>
    <td align="right">5.59</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">5.49</td>
    <td align="right">5.97</td>
    <td align="right">5.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">9.15</td>
    <td align="right">8.73</td>
    <td align="right">6.13</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">12.34</td>
    <td align="right">10.83</td>
    <td align="right">10.52</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">12.45</td>
    <td align="right">10.35</td>
    <td align="right">10.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">10.95</td>
    <td align="right">11.81</td>
    <td align="right">6.83</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">16.27</td>
    <td align="right">14.49</td>
    <td align="right">14.64</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">16.89</td>
    <td align="right">15.35</td>
    <td align="right">14.96</td>
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
    <td align="right">34.08</td>
    <td align="right">5.44</td>
    <td align="right">3.49</td>
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
    <td align="right">11.97</td>
    <td align="right">12.44</td>
    <td align="right">16.85</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.80</td>
    <td align="right">4.21</td>
    <td align="right">4.19</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.94</td>
    <td align="right">5.19</td>
    <td align="right">5.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.15</td>
    <td align="right">17.53</td>
    <td align="right">17.52</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.94</td>
    <td align="right">4.98</td>
    <td align="right">4.74</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.01</td>
    <td align="right">5.97</td>
    <td align="right">5.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.47</td>
    <td align="right">20.95</td>
    <td align="right">16.51</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.58</td>
    <td align="right">5.65</td>
    <td align="right">5.27</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.28</td>
    <td align="right">6.44</td>
    <td align="right">6.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.73</td>
    <td align="right">27.28</td>
    <td align="right">17.25</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.89</td>
    <td align="right">5.86</td>
    <td align="right">5.92</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.42</td>
    <td align="right">7.35</td>
    <td align="right">7.32</td>
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
    <td align="right">13.43</td>
    <td align="right">13.64</td>
    <td align="right">17.98</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">5.99</td>
    <td align="right">4.37</td>
    <td align="right">4.39</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">7.15</td>
    <td align="right">5.61</td>
    <td align="right">5.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">20.59</td>
    <td align="right">19.12</td>
    <td align="right">18.58</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">7.20</td>
    <td align="right">4.88</td>
    <td align="right">4.84</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">8.34</td>
    <td align="right">6.08</td>
    <td align="right">6.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">26.07</td>
    <td align="right">23.57</td>
    <td align="right">17.65</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">8.91</td>
    <td align="right">5.47</td>
    <td align="right">5.57</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">9.71</td>
    <td align="right">6.76</td>
    <td align="right">6.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">34.22</td>
    <td align="right">30.15</td>
    <td align="right">18.09</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">10.06</td>
    <td align="right">6.04</td>
    <td align="right">6.03</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">10.87</td>
    <td align="right">7.52</td>
    <td align="right">7.52</td>
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
    <td align="right">7.84</td>
    <td align="right">5.54</td>
    <td align="right">5.56</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.18</td>
    <td align="right">5.51</td>
    <td align="right">5.52</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.32</td>
    <td align="right">3.89</td>
    <td align="right">3.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.72</td>
    <td align="right">8.39</td>
    <td align="right">8.47</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.46</td>
    <td align="right">8.66</td>
    <td align="right">9.77</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.97</td>
    <td align="right">4.81</td>
    <td align="right">4.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.51</td>
    <td align="right">10.86</td>
    <td align="right">10.71</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.97</td>
    <td align="right">10.35</td>
    <td align="right">10.40</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.89</td>
    <td align="right">6.92</td>
    <td align="right">5.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">17.44</td>
    <td align="right">13.86</td>
    <td align="right">13.90</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">20.29</td>
    <td align="right">14.02</td>
    <td align="right">12.94</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.01</td>
    <td align="right">7.07</td>
    <td align="right">5.26</td>
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
    <td align="right">8.01</td>
    <td align="right">5.70</td>
    <td align="right">5.96</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">9.27</td>
    <td align="right">5.40</td>
    <td align="right">5.37</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">3.40</td>
    <td align="right">4.00</td>
    <td align="right">3.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">11.25</td>
    <td align="right">8.69</td>
    <td align="right">8.70</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">15.25</td>
    <td align="right">8.84</td>
    <td align="right">7.87</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.93</td>
    <td align="right">4.89</td>
    <td align="right">4.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">15.67</td>
    <td align="right">11.86</td>
    <td align="right">11.55</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">17.12</td>
    <td align="right">11.25</td>
    <td align="right">11.17</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">5.23</td>
    <td align="right">7.55</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">18.83</td>
    <td align="right">14.30</td>
    <td align="right">14.40</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">18.93</td>
    <td align="right">13.88</td>
    <td align="right">19.14</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">5.51</td>
    <td align="right">7.91</td>
    <td align="right">6.62</td>
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
    <td align="right">3.32</td>
    <td align="right">3.85</td>
    <td align="right">3.81</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.51</td>
    <td align="right">5.53</td>
    <td align="right">5.55</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.61</td>
    <td align="right">5.44</td>
    <td align="right">5.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.31</td>
    <td align="right">5.74</td>
    <td align="right">4.61</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.74</td>
    <td align="right">5.82</td>
    <td align="right">5.02</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.97</td>
    <td align="right">6.93</td>
    <td align="right">6.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.09</td>
    <td align="right">6.84</td>
    <td align="right">5.11</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.72</td>
    <td align="right">9.51</td>
    <td align="right">7.58</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.69</td>
    <td align="right">9.14</td>
    <td align="right">7.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.03</td>
    <td align="right">6.87</td>
    <td align="right">5.06</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">9.96</td>
    <td align="right">10.45</td>
    <td align="right">7.43</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">9.92</td>
    <td align="right">10.13</td>
    <td align="right">7.34</td>
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
    <td align="right">3.25</td>
    <td align="right">3.83</td>
    <td align="right">3.84</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">4.48</td>
    <td align="right">5.47</td>
    <td align="right">5.48</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">4.58</td>
    <td align="right">5.30</td>
    <td align="right">5.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.28</td>
    <td align="right">5.45</td>
    <td align="right">4.56</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">4.75</td>
    <td align="right">5.89</td>
    <td align="right">5.05</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">6.95</td>
    <td align="right">7.15</td>
    <td align="right">6.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">4.96</td>
    <td align="right">6.86</td>
    <td align="right">5.12</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">9.56</td>
    <td align="right">9.45</td>
    <td align="right">7.55</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">9.64</td>
    <td align="right">9.10</td>
    <td align="right">7.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">5.05</td>
    <td align="right">6.94</td>
    <td align="right">5.13</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">10.01</td>
    <td align="right">10.51</td>
    <td align="right">7.60</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">10.11</td>
    <td align="right">10.26</td>
    <td align="right">7.41</td>
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
    <td align="right">39.26</td>
    <td align="right">20.25</td>
    <td align="right">7.02</td>
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
    <td align="right">14.33</td>
    <td align="right">12.77</td>
    <td align="right">17.54</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.94</td>
    <td align="right">4.43</td>
    <td align="right">4.45</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.93</td>
    <td align="right">5.50</td>
    <td align="right">5.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">21.87</td>
    <td align="right">18.57</td>
    <td align="right">18.29</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.48</td>
    <td align="right">5.06</td>
    <td align="right">5.03</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.13</td>
    <td align="right">6.28</td>
    <td align="right">6.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">27.55</td>
    <td align="right">23.26</td>
    <td align="right">17.14</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.09</td>
    <td align="right">5.65</td>
    <td align="right">5.70</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.47</td>
    <td align="right">6.95</td>
    <td align="right">6.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">37.81</td>
    <td align="right">33.36</td>
    <td align="right">18.19</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.50</td>
    <td align="right">7.63</td>
    <td align="right">7.70</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">12.75</td>
    <td align="right">9.30</td>
    <td align="right">9.16</td>
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
    <td align="right">15.51</td>
    <td align="right">14.23</td>
    <td align="right">18.88</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">7.21</td>
    <td align="right">4.62</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">8.46</td>
    <td align="right">5.90</td>
    <td align="right">5.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">24.00</td>
    <td align="right">20.38</td>
    <td align="right">19.64</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">8.73</td>
    <td align="right">5.20</td>
    <td align="right">5.20</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">10.04</td>
    <td align="right">6.47</td>
    <td align="right">6.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">29.89</td>
    <td align="right">25.98</td>
    <td align="right">18.40</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">10.43</td>
    <td align="right">5.92</td>
    <td align="right">5.81</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">11.37</td>
    <td align="right">7.35</td>
    <td align="right">7.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">40.03</td>
    <td align="right">35.77</td>
    <td align="right">19.29</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">14.43</td>
    <td align="right">7.20</td>
    <td align="right">7.23</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">13.62</td>
    <td align="right">9.11</td>
    <td align="right">9.06</td>
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
    <td align="right">6.25</td>
    <td align="right">6.24</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.41</td>
    <td align="right">6.24</td>
    <td align="right">6.21</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.76</td>
    <td align="right">4.17</td>
    <td align="right">4.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.68</td>
    <td align="right">9.79</td>
    <td align="right">10.07</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">17.10</td>
    <td align="right">9.20</td>
    <td align="right">9.19</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.16</td>
    <td align="right">5.20</td>
    <td align="right">4.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">18.07</td>
    <td align="right">13.35</td>
    <td align="right">12.56</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.14</td>
    <td align="right">11.44</td>
    <td align="right">11.40</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.58</td>
    <td align="right">7.53</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">20.63</td>
    <td align="right">17.54</td>
    <td align="right">17.34</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">21.17</td>
    <td align="right">15.03</td>
    <td align="right">14.14</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">7.30</td>
    <td align="right">9.29</td>
    <td align="right">7.40</td>
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
    <td align="right">9.43</td>
    <td align="right">6.31</td>
    <td align="right">6.32</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">9.55</td>
    <td align="right">5.88</td>
    <td align="right">5.67</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.78</td>
    <td align="right">4.24</td>
    <td align="right">4.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">13.41</td>
    <td align="right">10.03</td>
    <td align="right">10.04</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">16.61</td>
    <td align="right">9.17</td>
    <td align="right">8.47</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">3.28</td>
    <td align="right">5.23</td>
    <td align="right">4.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">17.38</td>
    <td align="right">12.62</td>
    <td align="right">13.22</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">17.57</td>
    <td align="right">11.92</td>
    <td align="right">11.88</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">5.97</td>
    <td align="right">7.62</td>
    <td align="right">5.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">20.99</td>
    <td align="right">17.33</td>
    <td align="right">17.49</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">21.65</td>
    <td align="right">15.68</td>
    <td align="right">15.50</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">7.76</td>
    <td align="right">9.74</td>
    <td align="right">7.74</td>
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
    <td align="right">3.69</td>
    <td align="right">4.02</td>
    <td align="right">4.07</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.81</td>
    <td align="right">5.83</td>
    <td align="right">5.88</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.07</td>
    <td align="right">5.75</td>
    <td align="right">5.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.78</td>
    <td align="right">5.89</td>
    <td align="right">4.98</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.33</td>
    <td align="right">6.26</td>
    <td align="right">5.44</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.49</td>
    <td align="right">7.43</td>
    <td align="right">6.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">5.88</td>
    <td align="right">7.65</td>
    <td align="right">5.90</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">10.69</td>
    <td align="right">10.04</td>
    <td align="right">8.23</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">10.69</td>
    <td align="right">10.30</td>
    <td align="right">8.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">7.44</td>
    <td align="right">8.90</td>
    <td align="right">7.09</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">12.81</td>
    <td align="right">12.84</td>
    <td align="right">9.55</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.80</td>
    <td align="right">13.39</td>
    <td align="right">8.85</td>
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
    <td align="right">3.66</td>
    <td align="right">4.08</td>
    <td align="right">4.14</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">4.99</td>
    <td align="right">5.78</td>
    <td align="right">5.80</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">5.07</td>
    <td align="right">5.66</td>
    <td align="right">5.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">3.83</td>
    <td align="right">5.88</td>
    <td align="right">4.90</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">5.34</td>
    <td align="right">6.39</td>
    <td align="right">5.44</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">7.58</td>
    <td align="right">7.56</td>
    <td align="right">6.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">6.19</td>
    <td align="right">7.90</td>
    <td align="right">5.69</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">11.16</td>
    <td align="right">11.89</td>
    <td align="right">9.54</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">10.99</td>
    <td align="right">9.85</td>
    <td align="right">8.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">7.04</td>
    <td align="right">12.29</td>
    <td align="right">6.70</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">11.58</td>
    <td align="right">11.71</td>
    <td align="right">8.52</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">12.38</td>
    <td align="right">12.84</td>
    <td align="right">11.37</td>
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
    <td align="right">61.53</td>
    <td align="right">29.90</td>
    <td align="right">14.15</td>
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
    <td align="right">27.18</td>
    <td align="right">42.01</td>
    <td align="right">36.45</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.46</td>
    <td align="right">15.89</td>
    <td align="right">16.27</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.22</td>
    <td align="right">19.70</td>
    <td align="right">19.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.34</td>
    <td align="right">64.42</td>
    <td align="right">39.56</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.38</td>
    <td align="right">19.53</td>
    <td align="right">19.22</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.09</td>
    <td align="right">18.61</td>
    <td align="right">18.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.57</td>
    <td align="right">78.26</td>
    <td align="right">38.55</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.23</td>
    <td align="right">18.42</td>
    <td align="right">18.38</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.13</td>
    <td align="right">18.25</td>
    <td align="right">18.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">55.80</td>
    <td align="right">96.64</td>
    <td align="right">37.63</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.22</td>
    <td align="right">18.78</td>
    <td align="right">18.80</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.00</td>
    <td align="right">20.00</td>
    <td align="right">20.00</td>
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
    <td align="right">40.27</td>
    <td align="right">37.21</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">12.24</td>
    <td align="right">15.51</td>
    <td align="right">15.48</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">13.73</td>
    <td align="right">16.31</td>
    <td align="right">17.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">42.62</td>
    <td align="right">59.88</td>
    <td align="right">39.66</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">14.50</td>
    <td align="right">17.10</td>
    <td align="right">17.22</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">15.09</td>
    <td align="right">17.30</td>
    <td align="right">17.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">51.92</td>
    <td align="right">74.26</td>
    <td align="right">38.93</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">14.78</td>
    <td align="right">17.61</td>
    <td align="right">17.60</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">16.56</td>
    <td align="right">17.66</td>
    <td align="right">17.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">65.92</td>
    <td align="right">99.27</td>
    <td align="right">41.47</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">16.47</td>
    <td align="right">17.86</td>
    <td align="right">18.41</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">16.02</td>
    <td align="right">19.32</td>
    <td align="right">19.29</td>
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
    <td align="right">16.33</td>
    <td align="right">20.50</td>
    <td align="right">20.54</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.72</td>
    <td align="right">22.15</td>
    <td align="right">22.42</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.61</td>
    <td align="right">13.68</td>
    <td align="right">13.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.45</td>
    <td align="right">26.78</td>
    <td align="right">26.78</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.85</td>
    <td align="right">29.06</td>
    <td align="right">29.08</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.88</td>
    <td align="right">16.55</td>
    <td align="right">15.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.12</td>
    <td align="right">33.14</td>
    <td align="right">33.11</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.19</td>
    <td align="right">45.86</td>
    <td align="right">45.82</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.52</td>
    <td align="right">19.59</td>
    <td align="right">19.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.69</td>
    <td align="right">36.30</td>
    <td align="right">36.26</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.78</td>
    <td align="right">55.55</td>
    <td align="right">55.58</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.61</td>
    <td align="right">24.88</td>
    <td align="right">24.87</td>
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
    <td align="right">17.40</td>
    <td align="right">20.64</td>
    <td align="right">20.64</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">29.56</td>
    <td align="right">20.80</td>
    <td align="right">20.82</td>
    <td align="center">5</td>
    <td align="right">2.7323</td>
    <td align="right">11.47</td>
    <td align="right">14.36</td>
    <td align="right">14.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">21.46</td>
    <td align="right">26.75</td>
    <td align="right">26.72</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">40.43</td>
    <td align="right">27.84</td>
    <td align="right">27.87</td>
    <td align="center">8</td>
    <td align="right">0.5321</td>
    <td align="right">13.75</td>
    <td align="right">18.26</td>
    <td align="right">18.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">30.35</td>
    <td align="right">34.74</td>
    <td align="right">34.19</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">67.31</td>
    <td align="right">46.25</td>
    <td align="right">46.25</td>
    <td align="center">11</td>
    <td align="right">0.1189</td>
    <td align="right">16.28</td>
    <td align="right">19.96</td>
    <td align="right">19.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">35.19</td>
    <td align="right">36.88</td>
    <td align="right">36.90</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">78.76</td>
    <td align="right">55.33</td>
    <td align="right">55.36</td>
    <td align="center">13</td>
    <td align="right">0.0298</td>
    <td align="right">25.26</td>
    <td align="right">25.59</td>
    <td align="right">25.60</td>
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
    <td align="right">14.61</td>
    <td align="right">16.07</td>
    <td align="right">15.73</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.26</td>
    <td align="right">20.51</td>
    <td align="right">20.52</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.78</td>
    <td align="right">22.17</td>
    <td align="right">22.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.14</td>
    <td align="right">20.26</td>
    <td align="right">20.25</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.46</td>
    <td align="right">26.78</td>
    <td align="right">26.76</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.84</td>
    <td align="right">29.07</td>
    <td align="right">29.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.91</td>
    <td align="right">24.92</td>
    <td align="right">24.98</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.27</td>
    <td align="right">33.12</td>
    <td align="right">33.14</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.21</td>
    <td align="right">45.93</td>
    <td align="right">46.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">34.51</td>
    <td align="right">35.30</td>
    <td align="right">35.26</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.67</td>
    <td align="right">36.23</td>
    <td align="right">36.28</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.81</td>
    <td align="right">55.56</td>
    <td align="right">55.58</td>
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
    <td align="right">16.10</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">17.34</td>
    <td align="right">20.68</td>
    <td align="right">20.65</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">29.51</td>
    <td align="right">20.76</td>
    <td align="right">20.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4318</td>
    <td align="right">20.28</td>
    <td align="right">20.36</td>
    <td align="right">20.37</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">21.46</td>
    <td align="right">26.77</td>
    <td align="right">26.75</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">40.37</td>
    <td align="right">27.82</td>
    <td align="right">28.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0968</td>
    <td align="right">28.66</td>
    <td align="right">23.41</td>
    <td align="right">23.40</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">30.35</td>
    <td align="right">34.73</td>
    <td align="right">34.21</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">67.31</td>
    <td align="right">46.36</td>
    <td align="right">46.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">34.85</td>
    <td align="right">35.27</td>
    <td align="right">35.35</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">35.12</td>
    <td align="right">36.91</td>
    <td align="right">36.93</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">78.70</td>
    <td align="right">55.28</td>
    <td align="right">55.27</td>
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
    <td align="right">71.43</td>
    <td align="right">101.58</td>
    <td align="right">17.89</td>
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
    <td align="right">28.00</td>
    <td align="right">43.61</td>
    <td align="right">39.85</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.92</td>
    <td align="right">16.96</td>
    <td align="right">16.32</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.59</td>
    <td align="right">19.83</td>
    <td align="right">19.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">36.64</td>
    <td align="right">62.97</td>
    <td align="right">40.93</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.45</td>
    <td align="right">19.65</td>
    <td align="right">19.42</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.11</td>
    <td align="right">18.79</td>
    <td align="right">18.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">44.98</td>
    <td align="right">78.63</td>
    <td align="right">39.75</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">17.89</td>
    <td align="right">19.33</td>
    <td align="right">19.21</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">19.01</td>
    <td align="right">19.34</td>
    <td align="right">19.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">64.92</td>
    <td align="right">105.82</td>
    <td align="right">42.32</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">21.61</td>
    <td align="right">22.30</td>
    <td align="right">23.01</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">23.02</td>
    <td align="right">25.02</td>
    <td align="right">24.46</td>
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
    <td align="right">28.52</td>
    <td align="right">41.73</td>
    <td align="right">40.62</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">12.35</td>
    <td align="right">15.77</td>
    <td align="right">15.75</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">13.90</td>
    <td align="right">16.42</td>
    <td align="right">16.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">42.22</td>
    <td align="right">58.23</td>
    <td align="right">41.24</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">14.51</td>
    <td align="right">16.66</td>
    <td align="right">16.97</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">15.21</td>
    <td align="right">17.44</td>
    <td align="right">17.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">52.62</td>
    <td align="right">74.51</td>
    <td align="right">40.88</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">15.22</td>
    <td align="right">18.32</td>
    <td align="right">18.08</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">17.38</td>
    <td align="right">18.13</td>
    <td align="right">18.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">91.50</td>
    <td align="right">126.95</td>
    <td align="right">53.49</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">25.64</td>
    <td align="right">28.13</td>
    <td align="right">22.56</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">19.54</td>
    <td align="right">25.03</td>
    <td align="right">23.88</td>
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
    <td align="right">16.86</td>
    <td align="right">21.17</td>
    <td align="right">21.23</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.97</td>
    <td align="right">23.18</td>
    <td align="right">23.18</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">10.96</td>
    <td align="right">14.11</td>
    <td align="right">14.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.77</td>
    <td align="right">27.01</td>
    <td align="right">26.16</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">42.43</td>
    <td align="right">29.89</td>
    <td align="right">29.96</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.75</td>
    <td align="right">16.49</td>
    <td align="right">15.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">31.27</td>
    <td align="right">35.81</td>
    <td align="right">35.40</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">66.67</td>
    <td align="right">48.27</td>
    <td align="right">48.63</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">15.19</td>
    <td align="right">19.99</td>
    <td align="right">20.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">39.58</td>
    <td align="right">44.47</td>
    <td align="right">45.32</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">84.38</td>
    <td align="right">61.02</td>
    <td align="right">62.77</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">30.37</td>
    <td align="right">31.32</td>
    <td align="right">31.87</td>
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
    <td align="right">17.93</td>
    <td align="right">21.96</td>
    <td align="right">21.82</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">32.05</td>
    <td align="right">22.25</td>
    <td align="right">22.23</td>
    <td align="center">5</td>
    <td align="right">2.7367</td>
    <td align="right">11.74</td>
    <td align="right">14.66</td>
    <td align="right">14.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">21.50</td>
    <td align="right">26.10</td>
    <td align="right">26.00</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">42.65</td>
    <td align="right">28.63</td>
    <td align="right">28.64</td>
    <td align="center">8</td>
    <td align="right">0.5431</td>
    <td align="right">13.68</td>
    <td align="right">18.33</td>
    <td align="right">18.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">31.91</td>
    <td align="right">37.52</td>
    <td align="right">36.92</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">70.90</td>
    <td align="right">49.00</td>
    <td align="right">48.70</td>
    <td align="center">11</td>
    <td align="right">0.1181</td>
    <td align="right">16.56</td>
    <td align="right">20.51</td>
    <td align="right">20.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">40.01</td>
    <td align="right">59.06</td>
    <td align="right">59.69</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">87.58</td>
    <td align="right">60.56</td>
    <td align="right">60.38</td>
    <td align="center">13</td>
    <td align="right">0.0278</td>
    <td align="right">34.01</td>
    <td align="right">32.82</td>
    <td align="right">33.05</td>
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
    <td align="right">15.79</td>
    <td align="right">16.80</td>
    <td align="right">16.35</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.70</td>
    <td align="right">21.27</td>
    <td align="right">21.18</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.67</td>
    <td align="right">23.22</td>
    <td align="right">23.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">19.58</td>
    <td align="right">20.32</td>
    <td align="right">20.48</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.85</td>
    <td align="right">26.06</td>
    <td align="right">26.36</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">42.12</td>
    <td align="right">30.07</td>
    <td align="right">29.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">29.48</td>
    <td align="right">25.60</td>
    <td align="right">25.89</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">30.45</td>
    <td align="right">36.64</td>
    <td align="right">36.34</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">66.44</td>
    <td align="right">48.27</td>
    <td align="right">48.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">47.34</td>
    <td align="right">50.24</td>
    <td align="right">49.79</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">38.48</td>
    <td align="right">43.21</td>
    <td align="right">43.24</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">87.94</td>
    <td align="right">67.32</td>
    <td align="right">63.08</td>
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
    <td align="right">16.24</td>
    <td align="right">16.58</td>
    <td align="right">16.57</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">17.78</td>
    <td align="right">21.81</td>
    <td align="right">21.79</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">31.87</td>
    <td align="right">22.34</td>
    <td align="right">22.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4426</td>
    <td align="right">20.23</td>
    <td align="right">20.61</td>
    <td align="right">20.56</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">21.37</td>
    <td align="right">26.09</td>
    <td align="right">26.31</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">42.40</td>
    <td align="right">28.61</td>
    <td align="right">28.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0868</td>
    <td align="right">31.14</td>
    <td align="right">26.50</td>
    <td align="right">25.51</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">32.14</td>
    <td align="right">38.19</td>
    <td align="right">37.70</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">72.11</td>
    <td align="right">51.73</td>
    <td align="right">49.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">48.04</td>
    <td align="right">58.28</td>
    <td align="right">61.99</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">39.83</td>
    <td align="right">45.08</td>
    <td align="right">43.64</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">87.62</td>
    <td align="right">61.06</td>
    <td align="right">62.04</td>
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
    <td align="right">62.65</td>
    <td align="right">10.12</td>
    <td align="right">6.91</td>
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
    <td align="right">22.71</td>
    <td align="right">26.59</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.50</td>
    <td align="right">12.38</td>
    <td align="right">12.35</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.64</td>
    <td align="right">13.83</td>
    <td align="right">13.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.50</td>
    <td align="right">35.17</td>
    <td align="right">28.79</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.02</td>
    <td align="right">14.08</td>
    <td align="right">14.09</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.48</td>
    <td align="right">15.27</td>
    <td align="right">14.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.86</td>
    <td align="right">47.36</td>
    <td align="right">29.89</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.70</td>
    <td align="right">15.29</td>
    <td align="right">15.45</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.56</td>
    <td align="right">16.78</td>
    <td align="right">16.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">32.34</td>
    <td align="right">60.31</td>
    <td align="right">30.83</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.57</td>
    <td align="right">16.22</td>
    <td align="right">16.24</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.87</td>
    <td align="right">17.80</td>
    <td align="right">17.70</td>
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
    <td align="right">19.06</td>
    <td align="right">27.81</td>
    <td align="right">28.34</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">9.56</td>
    <td align="right">12.34</td>
    <td align="right">12.37</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">12.60</td>
    <td align="right">14.62</td>
    <td align="right">14.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">28.16</td>
    <td align="right">41.93</td>
    <td align="right">30.77</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">12.75</td>
    <td align="right">14.96</td>
    <td align="right">14.92</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">14.39</td>
    <td align="right">15.85</td>
    <td align="right">15.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">34.28</td>
    <td align="right">53.34</td>
    <td align="right">30.01</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">14.57</td>
    <td align="right">16.22</td>
    <td align="right">16.21</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">15.27</td>
    <td align="right">17.21</td>
    <td align="right">17.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">47.85</td>
    <td align="right">67.35</td>
    <td align="right">31.78</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">15.43</td>
    <td align="right">17.20</td>
    <td align="right">17.24</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">16.76</td>
    <td align="right">19.71</td>
    <td align="right">18.99</td>
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
    <td align="right">12.64</td>
    <td align="right">16.05</td>
    <td align="right">16.03</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.26</td>
    <td align="right">16.67</td>
    <td align="right">16.69</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.08</td>
    <td align="right">9.33</td>
    <td align="right">9.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.29</td>
    <td align="right">22.44</td>
    <td align="right">22.43</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.27</td>
    <td align="right">22.32</td>
    <td align="right">22.36</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.85</td>
    <td align="right">13.91</td>
    <td align="right">13.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.99</td>
    <td align="right">31.96</td>
    <td align="right">31.95</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.54</td>
    <td align="right">30.52</td>
    <td align="right">30.50</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.41</td>
    <td align="right">17.55</td>
    <td align="right">17.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.81</td>
    <td align="right">35.55</td>
    <td align="right">35.55</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.08</td>
    <td align="right">35.65</td>
    <td align="right">35.65</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.21</td>
    <td align="right">20.49</td>
    <td align="right">20.38</td>
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
    <td align="right">13.28</td>
    <td align="right">16.83</td>
    <td align="right">16.87</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">14.19</td>
    <td align="right">16.31</td>
    <td align="right">16.32</td>
    <td align="center">5</td>
    <td align="right">2.7323</td>
    <td align="right">7.05</td>
    <td align="right">9.29</td>
    <td align="right">9.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">18.32</td>
    <td align="right">25.44</td>
    <td align="right">25.46</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">19.44</td>
    <td align="right">23.75</td>
    <td align="right">23.74</td>
    <td align="center">8</td>
    <td align="right">0.5321</td>
    <td align="right">10.88</td>
    <td align="right">13.31</td>
    <td align="right">13.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">24.93</td>
    <td align="right">32.62</td>
    <td align="right">32.29</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">27.69</td>
    <td align="right">31.09</td>
    <td align="right">30.85</td>
    <td align="center">11</td>
    <td align="right">0.1189</td>
    <td align="right">13.19</td>
    <td align="right">17.89</td>
    <td align="right">17.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">28.29</td>
    <td align="right">35.84</td>
    <td align="right">35.85</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">34.09</td>
    <td align="right">38.03</td>
    <td align="right">38.06</td>
    <td align="center">13</td>
    <td align="right">0.0298</td>
    <td align="right">17.44</td>
    <td align="right">20.68</td>
    <td align="right">20.69</td>
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
    <td align="right">9.32</td>
    <td align="right">9.33</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.60</td>
    <td align="right">16.01</td>
    <td align="right">16.02</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.27</td>
    <td align="right">16.71</td>
    <td align="right">16.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">12.35</td>
    <td align="right">13.68</td>
    <td align="right">13.66</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.33</td>
    <td align="right">22.45</td>
    <td align="right">22.44</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.27</td>
    <td align="right">22.35</td>
    <td align="right">22.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.43</td>
    <td align="right">17.56</td>
    <td align="right">17.60</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.82</td>
    <td align="right">31.95</td>
    <td align="right">31.96</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.52</td>
    <td align="right">30.52</td>
    <td align="right">30.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.01</td>
    <td align="right">21.06</td>
    <td align="right">20.96</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.93</td>
    <td align="right">35.59</td>
    <td align="right">35.59</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.09</td>
    <td align="right">35.62</td>
    <td align="right">35.71</td>
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
    <td align="right">6.70</td>
    <td align="right">9.45</td>
    <td align="right">9.45</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">13.47</td>
    <td align="right">16.81</td>
    <td align="right">16.82</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">14.19</td>
    <td align="right">16.36</td>
    <td align="right">16.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4318</td>
    <td align="right">12.32</td>
    <td align="right">13.82</td>
    <td align="right">13.81</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">17.86</td>
    <td align="right">25.43</td>
    <td align="right">25.42</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">19.43</td>
    <td align="right">23.78</td>
    <td align="right">23.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0968</td>
    <td align="right">14.48</td>
    <td align="right">17.43</td>
    <td align="right">17.49</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">24.86</td>
    <td align="right">32.57</td>
    <td align="right">32.33</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">27.63</td>
    <td align="right">31.03</td>
    <td align="right">30.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">17.17</td>
    <td align="right">20.62</td>
    <td align="right">20.60</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">28.21</td>
    <td align="right">35.82</td>
    <td align="right">35.83</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">34.12</td>
    <td align="right">38.09</td>
    <td align="right">38.06</td>
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
    <td align="right">72.68</td>
    <td align="right">41.30</td>
    <td align="right">9.82</td>
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
    <td align="right">14.03</td>
    <td align="right">22.58</td>
    <td align="right">28.02</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.62</td>
    <td align="right">12.44</td>
    <td align="right">12.48</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">11.75</td>
    <td align="right">13.93</td>
    <td align="right">13.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">18.93</td>
    <td align="right">34.07</td>
    <td align="right">28.99</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">11.74</td>
    <td align="right">13.72</td>
    <td align="right">13.63</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.18</td>
    <td align="right">14.79</td>
    <td align="right">14.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.15</td>
    <td align="right">47.10</td>
    <td align="right">29.80</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">13.39</td>
    <td align="right">14.77</td>
    <td align="right">14.77</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">14.11</td>
    <td align="right">16.16</td>
    <td align="right">16.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">31.50</td>
    <td align="right">60.27</td>
    <td align="right">30.33</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">14.30</td>
    <td align="right">15.71</td>
    <td align="right">15.66</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">15.41</td>
    <td align="right">17.28</td>
    <td align="right">17.18</td>
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
    <td align="right">19.24</td>
    <td align="right">27.68</td>
    <td align="right">30.10</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">9.65</td>
    <td align="right">12.51</td>
    <td align="right">12.53</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">12.65</td>
    <td align="right">14.59</td>
    <td align="right">14.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">27.01</td>
    <td align="right">40.10</td>
    <td align="right">31.17</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">12.86</td>
    <td align="right">14.52</td>
    <td align="right">14.55</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">14.06</td>
    <td align="right">15.32</td>
    <td align="right">15.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">33.07</td>
    <td align="right">51.54</td>
    <td align="right">29.84</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">14.23</td>
    <td align="right">15.57</td>
    <td align="right">15.52</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">14.81</td>
    <td align="right">16.57</td>
    <td align="right">16.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">46.19</td>
    <td align="right">65.14</td>
    <td align="right">31.34</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">15.17</td>
    <td align="right">17.70</td>
    <td align="right">19.05</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">17.31</td>
    <td align="right">24.31</td>
    <td align="right">32.84</td>
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
    <td align="right">12.57</td>
    <td align="right">16.54</td>
    <td align="right">16.54</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.30</td>
    <td align="right">17.37</td>
    <td align="right">17.37</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.27</td>
    <td align="right">9.42</td>
    <td align="right">9.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.04</td>
    <td align="right">21.73</td>
    <td align="right">21.67</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.29</td>
    <td align="right">22.80</td>
    <td align="right">24.89</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.59</td>
    <td align="right">15.62</td>
    <td align="right">15.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.10</td>
    <td align="right">52.45</td>
    <td align="right">40.36</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">29.85</td>
    <td align="right">35.96</td>
    <td align="right">36.17</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">15.74</td>
    <td align="right">19.77</td>
    <td align="right">19.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">32.54</td>
    <td align="right">43.73</td>
    <td align="right">41.97</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">39.65</td>
    <td align="right">43.35</td>
    <td align="right">41.65</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">21.54</td>
    <td align="right">29.18</td>
    <td align="right">29.43</td>
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
    <td align="right">14.84</td>
    <td align="right">18.29</td>
    <td align="right">18.42</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">16.17</td>
    <td align="right">17.97</td>
    <td align="right">17.83</td>
    <td align="center">5</td>
    <td align="right">2.7367</td>
    <td align="right">7.17</td>
    <td align="right">10.13</td>
    <td align="right">9.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">19.61</td>
    <td align="right">26.64</td>
    <td align="right">27.26</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">22.42</td>
    <td align="right">25.00</td>
    <td align="right">24.47</td>
    <td align="center">8</td>
    <td align="right">0.5431</td>
    <td align="right">12.53</td>
    <td align="right">13.95</td>
    <td align="right">14.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">28.53</td>
    <td align="right">39.11</td>
    <td align="right">39.33</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">34.79</td>
    <td align="right">41.94</td>
    <td align="right">38.51</td>
    <td align="center">11</td>
    <td align="right">0.1181</td>
    <td align="right">19.53</td>
    <td align="right">20.29</td>
    <td align="right">22.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">36.97</td>
    <td align="right">51.76</td>
    <td align="right">47.25</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">43.03</td>
    <td align="right">51.86</td>
    <td align="right">58.97</td>
    <td align="center">13</td>
    <td align="right">0.0278</td>
    <td align="right">26.78</td>
    <td align="right">28.08</td>
    <td align="right">29.13</td>
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
    <td align="right">6.93</td>
    <td align="right">9.93</td>
    <td align="right">9.98</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.79</td>
    <td align="right">18.19</td>
    <td align="right">17.89</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">14.89</td>
    <td align="right">18.72</td>
    <td align="right">19.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">12.70</td>
    <td align="right">14.94</td>
    <td align="right">14.72</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">18.11</td>
    <td align="right">23.15</td>
    <td align="right">23.58</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">20.86</td>
    <td align="right">24.95</td>
    <td align="right">24.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">14.52</td>
    <td align="right">19.98</td>
    <td align="right">20.36</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">27.49</td>
    <td align="right">37.11</td>
    <td align="right">37.44</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">29.48</td>
    <td align="right">34.66</td>
    <td align="right">35.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">22.66</td>
    <td align="right">31.84</td>
    <td align="right">27.39</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">31.90</td>
    <td align="right">42.39</td>
    <td align="right">43.17</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">43.14</td>
    <td align="right">41.09</td>
    <td align="right">43.44</td>
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
    <td align="right">7.20</td>
    <td align="right">10.24</td>
    <td align="right">9.95</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">14.51</td>
    <td align="right">20.00</td>
    <td align="right">18.41</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">17.05</td>
    <td align="right">17.97</td>
    <td align="right">17.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4426</td>
    <td align="right">12.96</td>
    <td align="right">14.93</td>
    <td align="right">14.49</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">19.68</td>
    <td align="right">26.65</td>
    <td align="right">27.07</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">25.77</td>
    <td align="right">25.18</td>
    <td align="right">24.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0868</td>
    <td align="right">16.97</td>
    <td align="right">19.16</td>
    <td align="right">19.89</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">29.40</td>
    <td align="right">39.14</td>
    <td align="right">38.58</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">33.06</td>
    <td align="right">36.78</td>
    <td align="right">36.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">25.31</td>
    <td align="right">27.88</td>
    <td align="right">27.01</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">34.56</td>
    <td align="right">59.74</td>
    <td align="right">55.80</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">41.25</td>
    <td align="right">48.13</td>
    <td align="right">45.95</td>
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
    <td align="right">46.52</td>
    <td align="right">14.42</td>
    <td align="right">8.62</td>
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
    <td align="right">60.18</td>
    <td align="right">55.23</td>
    <td align="right">41.76</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">22.17</td>
    <td align="right">20.83</td>
    <td align="right">24.90</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">25.58</td>
    <td align="right">26.61</td>
    <td align="right">29.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">90.43</td>
    <td align="right">85.72</td>
    <td align="right">46.65</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">24.35</td>
    <td align="right">22.03</td>
    <td align="right">24.53</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">27.15</td>
    <td align="right">29.00</td>
    <td align="right">30.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">111.12</td>
    <td align="right">101.57</td>
    <td align="right">45.94</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.35</td>
    <td align="right">22.82</td>
    <td align="right">24.35</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.75</td>
    <td align="right">31.77</td>
    <td align="right">31.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">142.82</td>
    <td align="right">124.63</td>
    <td align="right">44.28</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">28.54</td>
    <td align="right">24.38</td>
    <td align="right">25.25</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">32.04</td>
    <td align="right">34.64</td>
    <td align="right">34.08</td>
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
    <td align="right">92.27</td>
    <td align="right">84.07</td>
    <td align="right">54.71</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">27.17</td>
    <td align="right">25.49</td>
    <td align="right">29.94</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">30.64</td>
    <td align="right">30.30</td>
    <td align="right">32.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">144.82</td>
    <td align="right">124.50</td>
    <td align="right">56.91</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">30.04</td>
    <td align="right">27.61</td>
    <td align="right">29.74</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">33.34</td>
    <td align="right">32.10</td>
    <td align="right">33.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">174.44</td>
    <td align="right">148.65</td>
    <td align="right">54.98</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">30.68</td>
    <td align="right">27.99</td>
    <td align="right">29.25</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">34.97</td>
    <td align="right">35.02</td>
    <td align="right">35.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">226.96</td>
    <td align="right">189.82</td>
    <td align="right">55.86</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">33.48</td>
    <td align="right">29.75</td>
    <td align="right">30.65</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">37.37</td>
    <td align="right">36.72</td>
    <td align="right">37.32</td>
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
    <td align="right">23.67</td>
    <td align="right">46.00</td>
    <td align="right">45.68</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.03</td>
    <td align="right">46.42</td>
    <td align="right">47.47</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.72</td>
    <td align="right">25.49</td>
    <td align="right">25.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.42</td>
    <td align="right">61.19</td>
    <td align="right">61.54</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.83</td>
    <td align="right">62.07</td>
    <td align="right">62.48</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.87</td>
    <td align="right">36.95</td>
    <td align="right">26.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">41.16</td>
    <td align="right">81.44</td>
    <td align="right">83.57</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">45.77</td>
    <td align="right">82.38</td>
    <td align="right">81.91</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.14</td>
    <td align="right">55.51</td>
    <td align="right">39.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">44.41</td>
    <td align="right">93.00</td>
    <td align="right">92.41</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">51.82</td>
    <td align="right">98.24</td>
    <td align="right">98.73</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.91</td>
    <td align="right">56.19</td>
    <td align="right">40.38</td>
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
    <td align="right">28.50</td>
    <td align="right">46.62</td>
    <td align="right">47.28</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">32.68</td>
    <td align="right">47.78</td>
    <td align="right">48.58</td>
    <td align="center">5</td>
    <td align="right">2.7313</td>
    <td align="right">22.62</td>
    <td align="right">27.08</td>
    <td align="right">26.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">32.81</td>
    <td align="right">63.01</td>
    <td align="right">63.12</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">40.18</td>
    <td align="right">63.93</td>
    <td align="right">64.89</td>
    <td align="center">8</td>
    <td align="right">0.5366</td>
    <td align="right">22.83</td>
    <td align="right">38.60</td>
    <td align="right">26.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">44.97</td>
    <td align="right">84.97</td>
    <td align="right">85.73</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">51.38</td>
    <td align="right">85.71</td>
    <td align="right">87.23</td>
    <td align="center">11</td>
    <td align="right">0.1134</td>
    <td align="right">32.14</td>
    <td align="right">55.84</td>
    <td align="right">39.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">48.71</td>
    <td align="right">97.37</td>
    <td align="right">97.08</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">57.49</td>
    <td align="right">102.17</td>
    <td align="right">103.32</td>
    <td align="center">13</td>
    <td align="right">0.0253</td>
    <td align="right">32.25</td>
    <td align="right">56.86</td>
    <td align="right">40.29</td>
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
    <td align="right">18.61</td>
    <td align="right">26.23</td>
    <td align="right">26.30</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.67</td>
    <td align="right">29.33</td>
    <td align="right">29.28</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.95</td>
    <td align="right">31.14</td>
    <td align="right">31.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">19.08</td>
    <td align="right">46.84</td>
    <td align="right">34.90</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.52</td>
    <td align="right">40.19</td>
    <td align="right">27.77</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.19</td>
    <td align="right">52.49</td>
    <td align="right">39.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">29.07</td>
    <td align="right">54.84</td>
    <td align="right">38.92</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.12</td>
    <td align="right">53.15</td>
    <td align="right">35.16</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.21</td>
    <td align="right">61.52</td>
    <td align="right">43.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">29.20</td>
    <td align="right">55.59</td>
    <td align="right">39.69</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">34.10</td>
    <td align="right">65.72</td>
    <td align="right">45.10</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.62</td>
    <td align="right">63.67</td>
    <td align="right">44.91</td>
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
    <td align="right">22.61</td>
    <td align="right">27.54</td>
    <td align="right">27.42</td>
    <td align="center">5</td>
    <td align="right">2.4471</td>
    <td align="right">23.95</td>
    <td align="right">29.28</td>
    <td align="right">29.45</td>
    <td align="center">5</td>
    <td align="right">2.3272</td>
    <td align="right">24.32</td>
    <td align="right">30.55</td>
    <td align="right">30.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4375</td>
    <td align="right">23.70</td>
    <td align="right">47.84</td>
    <td align="right">35.93</td>
    <td align="center">8</td>
    <td align="right">0.4137</td>
    <td align="right">23.45</td>
    <td align="right">40.49</td>
    <td align="right">28.03</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">25.21</td>
    <td align="right">54.81</td>
    <td align="right">40.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0906</td>
    <td align="right">31.24</td>
    <td align="right">55.75</td>
    <td align="right">39.51</td>
    <td align="center">11</td>
    <td align="right">0.0740</td>
    <td align="right">34.90</td>
    <td align="right">62.41</td>
    <td align="right">44.54</td>
    <td align="center">11</td>
    <td align="right">0.0604</td>
    <td align="right">34.68</td>
    <td align="right">62.15</td>
    <td align="right">43.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">31.79</td>
    <td align="right">56.61</td>
    <td align="right">40.55</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">35.45</td>
    <td align="right">66.32</td>
    <td align="right">45.74</td>
    <td align="center">14</td>
    <td align="right">0.0129</td>
    <td align="right">35.54</td>
    <td align="right">65.80</td>
    <td align="right">45.17</td>
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
    <td align="right">75.49</td>
    <td align="right">37.86</td>
    <td align="right">18.63</td>
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
    <td align="right">76.49</td>
    <td align="right">62.72</td>
    <td align="right">47.61</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">26.65</td>
    <td align="right">25.44</td>
    <td align="right">31.30</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">32.54</td>
    <td align="right">34.34</td>
    <td align="right">39.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">128.37</td>
    <td align="right">129.29</td>
    <td align="right">59.21</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">44.77</td>
    <td align="right">36.93</td>
    <td align="right">43.82</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">62.03</td>
    <td align="right">59.19</td>
    <td align="right">64.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">277.91</td>
    <td align="right">231.63</td>
    <td align="right">76.50</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">59.36</td>
    <td align="right">45.22</td>
    <td align="right">43.49</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">68.45</td>
    <td align="right">68.77</td>
    <td align="right">74.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">423.99</td>
    <td align="right">366.84</td>
    <td align="right">90.16</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">86.63</td>
    <td align="right">55.44</td>
    <td align="right">51.44</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">78.53</td>
    <td align="right">89.11</td>
    <td align="right">79.58</td>
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
    <td align="right">108.23</td>
    <td align="right">92.37</td>
    <td align="right">59.42</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">32.09</td>
    <td align="right">27.23</td>
    <td align="right">33.35</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">37.48</td>
    <td align="right">36.47</td>
    <td align="right">39.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">203.98</td>
    <td align="right">169.91</td>
    <td align="right">72.01</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">47.46</td>
    <td align="right">39.43</td>
    <td align="right">43.13</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">51.07</td>
    <td align="right">52.07</td>
    <td align="right">53.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">400.57</td>
    <td align="right">293.21</td>
    <td align="right">90.92</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">64.17</td>
    <td align="right">54.19</td>
    <td align="right">55.58</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">80.80</td>
    <td align="right">81.39</td>
    <td align="right">79.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">660.02</td>
    <td align="right">510.09</td>
    <td align="right">113.70</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">88.20</td>
    <td align="right">63.13</td>
    <td align="right">62.31</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">86.07</td>
    <td align="right">87.85</td>
    <td align="right">87.06</td>
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
    <td align="right">29.26</td>
    <td align="right">52.87</td>
    <td align="right">51.23</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">35.37</td>
    <td align="right">57.78</td>
    <td align="right">62.23</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">22.48</td>
    <td align="right">36.70</td>
    <td align="right">38.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">63.52</td>
    <td align="right">93.59</td>
    <td align="right">91.27</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">87.66</td>
    <td align="right">96.83</td>
    <td align="right">98.76</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">25.92</td>
    <td align="right">60.11</td>
    <td align="right">48.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">66.99</td>
    <td align="right">103.85</td>
    <td align="right">106.59</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">77.08</td>
    <td align="right">107.41</td>
    <td align="right">107.11</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">74.47</td>
    <td align="right">120.13</td>
    <td align="right">106.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.73</td>
    <td align="right">129.22</td>
    <td align="right">131.45</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">110.54</td>
    <td align="right">147.01</td>
    <td align="right">147.52</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">91.20</td>
    <td align="right">127.34</td>
    <td align="right">114.18</td>
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
    <td align="right">38.74</td>
    <td align="right">79.76</td>
    <td align="right">68.69</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">40.36</td>
    <td align="right">58.52</td>
    <td align="right">58.84</td>
    <td align="center">5</td>
    <td align="right">2.7250</td>
    <td align="right">26.66</td>
    <td align="right">32.63</td>
    <td align="right">33.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">50.30</td>
    <td align="right">86.74</td>
    <td align="right">86.62</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">74.34</td>
    <td align="right">99.88</td>
    <td align="right">99.05</td>
    <td align="center">8</td>
    <td align="right">0.5385</td>
    <td align="right">37.43</td>
    <td align="right">66.92</td>
    <td align="right">50.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">68.27</td>
    <td align="right">120.78</td>
    <td align="right">119.32</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">97.11</td>
    <td align="right">119.04</td>
    <td align="right">113.12</td>
    <td align="center">11</td>
    <td align="right">0.1183</td>
    <td align="right">72.63</td>
    <td align="right">115.03</td>
    <td align="right">91.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">85.69</td>
    <td align="right">129.10</td>
    <td align="right">129.11</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">107.14</td>
    <td align="right">143.59</td>
    <td align="right">146.05</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">99.95</td>
    <td align="right">134.62</td>
    <td align="right">118.86</td>
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
    <td align="right">30.56</td>
    <td align="right">50.93</td>
    <td align="right">75.48</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">46.31</td>
    <td align="right">90.52</td>
    <td align="right">86.01</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">30.17</td>
    <td align="right">59.08</td>
    <td align="right">52.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">29.50</td>
    <td align="right">87.36</td>
    <td align="right">81.49</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">26.80</td>
    <td align="right">76.87</td>
    <td align="right">50.08</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">42.53</td>
    <td align="right">109.79</td>
    <td align="right">84.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">79.35</td>
    <td align="right">115.80</td>
    <td align="right">99.37</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">63.41</td>
    <td align="right">103.14</td>
    <td align="right">70.31</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">75.18</td>
    <td align="right">106.18</td>
    <td align="right">79.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">96.42</td>
    <td align="right">127.76</td>
    <td align="right">113.48</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">66.62</td>
    <td align="right">123.47</td>
    <td align="right">100.67</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">68.86</td>
    <td align="right">123.11</td>
    <td align="right">89.84</td>
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
    <td align="right">29.79</td>
    <td align="right">39.19</td>
    <td align="right">38.12</td>
    <td align="center">5</td>
    <td align="right">2.4405</td>
    <td align="right">34.22</td>
    <td align="right">40.67</td>
    <td align="right">43.19</td>
    <td align="center">5</td>
    <td align="right">2.3265</td>
    <td align="right">29.74</td>
    <td align="right">42.39</td>
    <td align="right">44.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4413</td>
    <td align="right">36.77</td>
    <td align="right">76.05</td>
    <td align="right">66.40</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">43.10</td>
    <td align="right">82.98</td>
    <td align="right">60.79</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">54.52</td>
    <td align="right">115.01</td>
    <td align="right">84.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0845</td>
    <td align="right">75.29</td>
    <td align="right">111.53</td>
    <td align="right">93.12</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">52.49</td>
    <td align="right">98.70</td>
    <td align="right">75.34</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">58.31</td>
    <td align="right">120.47</td>
    <td align="right">95.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">103.54</td>
    <td align="right">131.14</td>
    <td align="right">112.11</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">79.04</td>
    <td align="right">124.86</td>
    <td align="right">111.91</td>
    <td align="center">14</td>
    <td align="right">0.0116</td>
    <td align="right">78.71</td>
    <td align="right">122.83</td>
    <td align="right">114.89</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
